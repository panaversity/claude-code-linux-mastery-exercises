"""AI Support Agent - Main Application Entry Point"""

import os
import logging
from contextlib import asynccontextmanager

import yaml
from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from app.auth import verify_token
from app.models import ChatRequest, ChatResponse
from app.knowledge_base import KnowledgeBase
from app.ai_client import AIClient
from app.database import Database

logger = logging.getLogger(__name__)


def load_config():
    """Load application configuration from YAML file."""
    config_path = os.getenv("CONFIG_PATH", "/etc/agent-app/config.yaml")
    with open(config_path, "r") as f:
        return yaml.safe_load(f)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan handler for startup/shutdown."""
    config = load_config()

    # Initialize services
    app.state.db = Database(config["database"])
    app.state.kb = KnowledgeBase(config["knowledge_base"])
    app.state.ai = AIClient(
        api_key=os.getenv("DEEPSEEK_API_KEY"),
        model=config["ai_model"]["model"],
        temperature=config["ai_model"]["temperature"],
    )

    await app.state.db.connect()
    await app.state.kb.load_index()

    logger.info("Agent application started successfully")
    yield

    # Cleanup
    await app.state.db.disconnect()
    logger.info("Agent application shut down")


app = FastAPI(
    title="AI Support Agent",
    version="2.4.1",
    lifespan=lifespan,
)

config = load_config()
app.add_middleware(
    CORSMiddleware,
    allow_origins=config["cors"]["allowed_origins"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "ok", "version": "2.4.1"}


@app.post("/api/chat", response_model=ChatResponse)
async def chat(request: ChatRequest, user=Depends(verify_token)):
    """Handle chat requests."""
    try:
        context = await app.state.kb.search(request.message)
        response = await app.state.ai.generate(
            message=request.message,
            context=context,
            session_id=request.session_id,
        )
        await app.state.db.log_interaction(
            user_id=user.id,
            session_id=request.session_id,
            message=request.message,
            response=response.text,
            tokens=response.tokens_used,
            latency_ms=response.latency_ms,
        )
        return ChatResponse(
            text=response.text,
            tokens_used=response.tokens_used,
            session_id=request.session_id,
        )
    except Exception as e:
        logger.error(f"Chat error for user={user.id}: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")


@app.post("/api/feedback")
async def feedback(session_id: str, rating: int, user=Depends(verify_token)):
    """Record user feedback for a session."""
    await app.state.db.save_feedback(
        user_id=user.id,
        session_id=session_id,
        rating=rating,
    )
    return {"status": "recorded"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, workers=4)
