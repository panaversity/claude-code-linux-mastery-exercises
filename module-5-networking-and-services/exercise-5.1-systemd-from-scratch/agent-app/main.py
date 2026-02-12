#!/usr/bin/env python3
"""Customer Support Agent - FastAPI Application

A simple AI-powered customer support agent that answers questions
using a knowledge base and an LLM backend.
"""
import os
import logging
from datetime import datetime
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Customer Support Agent", version="1.0.0")
logger = logging.getLogger("support-agent")
logging.basicConfig(level=os.getenv("LOG_LEVEL", "INFO"))

# Configuration from environment
PORT = int(os.getenv("PORT", "8080"))
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4")
MAX_TOKENS = int(os.getenv("MAX_TOKENS", "2048"))
API_KEY = os.getenv("API_KEY", "")

class ChatRequest(BaseModel):
    message: str
    session_id: str = "default"

class ChatResponse(BaseModel):
    reply: str
    tokens_used: int
    model: str
    timestamp: str

@app.get("/health")
def health():
    return {"status": "ok", "uptime": "running", "model": MODEL_NAME}

@app.post("/api/chat")
def chat(request: ChatRequest):
    if not API_KEY:
        raise HTTPException(status_code=500, detail="API_KEY not configured")
    logger.info(f"Request: user_session={request.session_id} message_length={len(request.message)}")
    # Simulated response (would call LLM in production)
    reply = f"I'd be happy to help with: {request.message[:50]}..."
    return ChatResponse(
        reply=reply,
        tokens_used=len(reply.split()),
        model=MODEL_NAME,
        timestamp=datetime.utcnow().isoformat()
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=PORT)
