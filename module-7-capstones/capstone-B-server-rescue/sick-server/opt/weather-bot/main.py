#!/usr/bin/env python3
"""Weather Data Bot v1.0

Serves cached weather data via API. Data is refreshed by a cron job
that runs fetch-weather.sh periodically.

The bot itself is working fine. The issue is with the cron job that
feeds it fresh data.
"""
import os
import logging
from datetime import datetime
from fastapi import FastAPI

logger = logging.getLogger("weather-bot")

PORT = int(os.getenv("PORT", "9090"))
DATA_FILE = os.getenv("DATA_FILE", "/var/lib/weather-bot/weather-data.json")
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

logging.basicConfig(
    level=getattr(logging, LOG_LEVEL),
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)

app = FastAPI(title="Weather Data Bot", version="1.0.0")

# Track when data was last refreshed
last_fetch = datetime(2026, 2, 9, 18, 0, 3)  # Last successful cron run

@app.get("/health")
def health():
    staleness = (datetime.utcnow() - last_fetch).total_seconds() / 3600
    status = "healthy" if staleness < 2 else "degraded" if staleness < 6 else "stale"
    return {
        "status": status,
        "version": "1.0.0",
        "last_data_fetch": last_fetch.isoformat(),
        "data_staleness_hours": round(staleness, 1)
    }

@app.get("/api/weather/{city}")
def get_weather(city: str):
    staleness = (datetime.utcnow() - last_fetch).total_seconds() / 3600
    if staleness > 12:
        logger.warning(f"Weather data is {staleness:.0f} hours stale. Last successful fetch: {last_fetch.isoformat()}")
    return {
        "city": city,
        "temperature": 72,
        "conditions": "partly cloudy",
        "data_age_hours": round(staleness, 1),
        "warning": "DATA MAY BE STALE" if staleness > 2 else None
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=PORT)
