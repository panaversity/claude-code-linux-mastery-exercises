#!/usr/bin/env python3
"""Customer Support Agent - FastAPI Application

A simple AI-powered customer support agent that handles common
support queries and escalates complex issues to human agents.
"""

import os
import json
import logging
from datetime import datetime
from pathlib import Path

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Configuration
CONFIG_PATH = os.getenv("CONFIG_PATH", "/etc/customer-support-agent/config.yaml")
LOG_DIR = os.getenv("LOG_DIR", "/var/log/customer-support-agent")

app = FastAPI(title="Customer Support Agent", version="2.4.1")
logger = logging.getLogger("support-agent")


class ChatRequest(BaseModel):
    user_id: str
    message: str
    session_id: str | None = None


class ChatResponse(BaseModel):
    response: str
    confidence: float
    session_id: str
    escalated: bool = False


@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "version": "2.4.1",
        "timestamp": datetime.now().isoformat(),
    }


@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """Handle a customer support query."""
    logger.info(f"Query from {request.user_id}: {request.message[:50]}...")

    # Simplified response logic for exercise purposes
    confidence = 0.85
    response_text = f"Thank you for your question about: {request.message[:100]}"

    if confidence < 0.5:
        logger.warning(f"Low confidence ({confidence}) - escalating")
        return ChatResponse(
            response="I'm connecting you with a human agent for better assistance.",
            confidence=confidence,
            session_id=request.session_id or "auto-generated",
            escalated=True,
        )

    return ChatResponse(
        response=response_text,
        confidence=confidence,
        session_id=request.session_id or "auto-generated",
    )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8080)
