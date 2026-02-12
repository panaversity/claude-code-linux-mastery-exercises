#!/usr/bin/env python3
"""Customer Support Agent v2.0

Production FastAPI application for AI-powered customer support.
This application is FINE -- the issues are all infrastructure-related.
"""
import os
import json
import logging
from datetime import datetime
from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

logger = logging.getLogger("support-agent")

PORT = int(os.getenv("PORT", "8080"))
MODEL = os.getenv("MODEL_NAME", "gpt-4")
CACHE_FILE = os.getenv("CACHE_FILE", "/var/lib/support-agent/cache/response-cache.json")
API_KEY = os.getenv("API_KEY", "")
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

logging.basicConfig(
    level=getattr(logging, LOG_LEVEL),
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)

# Load cache into memory at startup
# NOTE: When cache file is 2GB+, this causes massive memory usage
# and slow startup times. There is no max cache size or eviction policy.
_cache = {}

@asynccontextmanager
async def lifespan(app: FastAPI):
    global _cache
    logger.info(f"Starting support-agent on port {PORT}")
    logger.info(f"Model: {MODEL}")
    try:
        with open(CACHE_FILE, "r") as f:
            data = json.load(f)
            if "cache_entries_sample" in data:
                _cache = {e["key"]: e for e in data["cache_entries_sample"]}
            logger.info(f"Loaded {len(_cache)} cache entries")
    except (FileNotFoundError, json.JSONDecodeError):
        logger.warning("Cache file not found or corrupt, starting with empty cache")
        _cache = {}
    yield
    logger.info("Shutting down support-agent")

app = FastAPI(title="Customer Support Agent", version="2.0.0", lifespan=lifespan)

class ChatRequest(BaseModel):
    message: str
    session_id: str = "default"
    user_id: str = "anonymous"

class ChatResponse(BaseModel):
    reply: str
    tokens_used: int
    model: str
    session_id: str
    timestamp: str

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "version": "2.0.0",
        "model": MODEL,
        "cache_entries": len(_cache),
        "uptime": "running"
    }

@app.post("/api/chat")
def chat(request: ChatRequest):
    if not API_KEY:
        raise HTTPException(500, "API_KEY not configured")
    logger.info(f"Chat request: user={request.user_id} session={request.session_id}")
    reply = f"Thank you for your question about: {request.message[:80]}. Let me help you with that."
    response = ChatResponse(
        reply=reply,
        tokens_used=len(reply.split()),
        model=MODEL,
        session_id=request.session_id,
        timestamp=datetime.utcnow().isoformat()
    )
    logger.info(f"Response: tokens={response.tokens_used} model={MODEL}")
    return response

@app.get("/api/stats")
def stats():
    return {"total_requests": 0, "avg_latency_ms": 0, "model": MODEL, "cache_size": len(_cache)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=PORT)
