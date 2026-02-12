#!/usr/bin/env python3
"""
Summarizer Agent - AI-powered text summarization service.

Accepts text input via REST API, generates summaries using an LLM,
and stores results in a local SQLite database.

WARNING: This file is deployed in /tmp which gets cleaned on reboot!
This should be in /opt/agent-app/ for persistence.

Usage:
    python3 main.py --config config.yaml
    python3 main.py --port 8080
"""

import os
import sys
import yaml
import json
import sqlite3
import logging
import hashlib
from datetime import datetime, timezone
from pathlib import Path

from flask import Flask, request, jsonify
from openai import OpenAI

# Load configuration
CONFIG_PATH = os.environ.get("CONFIG_PATH", "./config.yaml")

app = Flask(__name__)
logger = logging.getLogger("summarizer-agent")


def load_config(path: str) -> dict:
    """Load YAML configuration file."""
    with open(path, "r") as f:
        return yaml.safe_load(f)


def get_db_connection(db_path: str) -> sqlite3.Connection:
    """Create a database connection."""
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn


def init_db(db_path: str):
    """Initialize the database schema."""
    conn = get_db_connection(db_path)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS summaries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            input_hash TEXT UNIQUE NOT NULL,
            input_text TEXT NOT NULL,
            summary TEXT NOT NULL,
            model TEXT NOT NULL,
            tokens_used INTEGER,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()


@app.route("/health", methods=["GET"])
def health():
    """Health check endpoint."""
    return jsonify({
        "status": "healthy",
        "service": "summarizer-agent",
        "version": "2.1.0",
    })


@app.route("/summarize", methods=["POST"])
def summarize():
    """Summarize input text."""
    data = request.get_json()
    if not data or "text" not in data:
        return jsonify({"error": "Missing 'text' field"}), 400

    text = data["text"]
    max_length = data.get("max_length", 200)
    input_hash = hashlib.sha256(text.encode()).hexdigest()

    config = app.config["app_config"]

    # Check cache (database)
    db = get_db_connection(config["database"]["path"])
    cached = db.execute(
        "SELECT summary FROM summaries WHERE input_hash = ?", (input_hash,)
    ).fetchone()

    if cached:
        db.close()
        logger.info(f"Cache hit for hash {input_hash[:8]}...")
        return jsonify({"summary": cached["summary"], "cached": True})

    # Generate summary via LLM
    try:
        client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
        response = client.chat.completions.create(
            model=config["llm"]["model"],
            messages=[
                {"role": "system", "content": f"Summarize the following text in under {max_length} words. Be concise and capture the key points."},
                {"role": "user", "content": text},
            ],
            max_tokens=config["llm"]["max_tokens"],
            temperature=0.3,
        )

        summary = response.choices[0].message.content
        tokens = response.usage.total_tokens

        # Store in database
        db.execute(
            "INSERT INTO summaries (input_hash, input_text, summary, model, tokens_used) VALUES (?, ?, ?, ?, ?)",
            (input_hash, text, summary, config["llm"]["model"], tokens),
        )
        db.commit()
        db.close()

        logger.info(f"Generated summary: {tokens} tokens used")
        return jsonify({"summary": summary, "cached": False, "tokens_used": tokens})

    except Exception as e:
        logger.error(f"LLM error: {str(e)}")
        db.close()
        return jsonify({"error": "Failed to generate summary"}), 500


@app.route("/stats", methods=["GET"])
def stats():
    """Return usage statistics."""
    config = app.config["app_config"]
    db = get_db_connection(config["database"]["path"])

    total = db.execute("SELECT COUNT(*) as count FROM summaries").fetchone()["count"]
    tokens = db.execute("SELECT SUM(tokens_used) as total FROM summaries").fetchone()["total"] or 0
    db.close()

    return jsonify({
        "total_summaries": total,
        "total_tokens": tokens,
        "database": config["database"]["path"],
    })


def main():
    config = load_config(CONFIG_PATH)
    app.config["app_config"] = config

    logging.basicConfig(
        level=getattr(logging, config.get("logging", {}).get("level", "INFO")),
        format="%(asctime)s [%(name)s] %(levelname)s: %(message)s",
    )

    # Initialize database
    init_db(config["database"]["path"])

    port = config.get("server", {}).get("port", 8080)
    host = config.get("server", {}).get("host", "0.0.0.0")

    logger.info(f"Starting Summarizer Agent on {host}:{port}")
    app.run(host=host, port=port)


if __name__ == "__main__":
    main()
