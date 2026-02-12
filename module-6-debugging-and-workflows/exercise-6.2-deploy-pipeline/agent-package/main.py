#!/usr/bin/env python3
"""Customer Support Agent — FastAPI application."""

import os
import logging
from contextlib import asynccontextmanager

import redis.asyncio as aioredis
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

logger = logging.getLogger(__name__)

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4")
MAX_TOKENS = int(os.getenv("MAX_TOKENS", "2048"))
PORT = int(os.getenv("PORT", "8080"))


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Startup and shutdown lifecycle."""
    logger.info("Connecting to Redis at %s", REDIS_URL)
    try:
        app.state.redis = aioredis.from_url(REDIS_URL)
        await app.state.redis.ping()
        logger.info("Redis connection established")
    except Exception as e:
        logger.error("Failed to connect to Redis: %s", e)
        raise RuntimeError("Cannot start without Redis connection") from e

    yield

    logger.info("Shutting down, closing Redis connection")
    await app.state.redis.close()


app = FastAPI(title="Support Agent", lifespan=lifespan)


class ChatRequest(BaseModel):
    message: str
    session_id: str | None = None


class ChatResponse(BaseModel):
    reply: str
    session_id: str
    model: str


@app.get("/health")
async def health():
    """Health check endpoint."""
    try:
        await app.state.redis.ping()
        return {"status": "healthy", "model": MODEL_NAME}
    except Exception:
        raise HTTPException(status_code=503, detail="Redis unavailable")


@app.post("/api/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """Handle chat requests."""
    session_id = request.session_id or "new-session"

    # Check cache
    cache_key = f"chat:{session_id}:{hash(request.message)}"
    cached = await app.state.redis.get(cache_key)
    if cached:
        return ChatResponse(
            reply=cached.decode(), session_id=session_id, model=MODEL_NAME
        )

    # Simulate LLM response (in production, this calls the model API)
    reply = f"[{MODEL_NAME}] Response to: {request.message[:50]}"

    # Cache response
    await app.state.redis.setex(cache_key, 3600, reply)

    return ChatResponse(reply=reply, session_id=session_id, model=MODEL_NAME)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=PORT, log_level=os.getenv("LOG_LEVEL", "info").lower())
