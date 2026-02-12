#!/usr/bin/env python3
"""Simple Webhook Receiver

Receives POST webhooks, logs them to a JSONL file, and returns 200 OK.
Useful for testing integrations and monitoring event flows.

This is a deliberately simple application. The complexity in this capstone
is in the deployment, not the application code.
"""
import os
import json
import logging
from datetime import datetime
from fastapi import FastAPI, Request

app = FastAPI(title="Webhook Receiver", version="1.0.0")
logger = logging.getLogger("webhook-receiver")
logging.basicConfig(level=os.getenv("LOG_LEVEL", "INFO"))

PORT = int(os.getenv("PORT", "9000"))
WEBHOOK_LOG = os.getenv("WEBHOOK_LOG", "/var/log/webhook-receiver/webhooks.jsonl")

@app.get("/health")
def health():
    return {"status": "ok", "service": "webhook-receiver"}

@app.post("/webhook")
async def receive_webhook(request: Request):
    body = await request.json()
    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "source_ip": request.client.host,
        "headers": dict(request.headers),
        "body": body
    }
    logger.info(f"Webhook received from {request.client.host}")
    with open(WEBHOOK_LOG, "a") as f:
        f.write(json.dumps(entry) + "\n")
    return {"status": "received", "timestamp": entry["timestamp"]}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=PORT)
