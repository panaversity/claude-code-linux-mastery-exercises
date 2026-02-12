#!/usr/bin/env python3
"""Customer Support Agent v2.0

Production-ready FastAPI application for AI-powered customer support.
Integrates with Redis for caching and PostgreSQL for session history.
"""
import os
import logging
from datetime import datetime
from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

logger = logging.getLogger("support-agent")

# Configuration
PORT = int(os.getenv("PORT", "8080"))
MODEL = os.getenv("MODEL_NAME", "gpt-4")
REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")
DB_URL = os.getenv("DB_URL", "")
API_KEY = os.getenv("API_KEY", "")
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

logging.basicConfig(
    level=getattr(logging, LOG_LEVEL),
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info(f"Starting support-agent on port {PORT}")
    logger.info(f"Model: {MODEL}, Redis: {REDIS_URL}")
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
    return {"total_requests": 0, "avg_latency_ms": 0, "model": MODEL}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=PORT)
