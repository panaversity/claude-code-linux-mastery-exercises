#!/usr/bin/env python3
"""
Weather Bot - Real-time weather data aggregation agent.

Fetches weather data from OpenWeatherMap API for configured cities
and serves it via a REST API on port 8001.

Usage:
    python3 main.py
    python3 main.py --config /etc/weather-bot/config.yaml
"""

import os
import sys
import yaml
import json
import logging
import asyncio
from datetime import datetime, timezone
from pathlib import Path

import aiohttp
from aiohttp import web

# Load configuration
CONFIG_PATH = os.environ.get("CONFIG_PATH", "/etc/weather-bot/config.yaml")

logger = logging.getLogger("weather-bot")


def load_config(path: str) -> dict:
    with open(path, "r") as f:
        return yaml.safe_load(f)


class WeatherCache:
    """In-memory cache with Redis fallback."""

    def __init__(self):
        self._cache = {}
        self._timestamps = {}

    def get(self, city: str) -> dict | None:
        if city in self._cache:
            age = (datetime.now(timezone.utc) - self._timestamps[city]).seconds
            if age < 600:
                return self._cache[city]
        return None

    def set(self, city: str, data: dict):
        self._cache[city] = data
        self._timestamps[city] = datetime.now(timezone.utc)


cache = WeatherCache()


async def fetch_weather(session: aiohttp.ClientSession, city: dict, api_key: str) -> dict:
    """Fetch weather data for a single city."""
    cached = cache.get(city["name"])
    if cached:
        logger.debug(f"Cache hit for {city['name']}")
        return cached

    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "lat": city["lat"],
        "lon": city["lon"],
        "appid": api_key,
        "units": "metric",
    }

    try:
        async with session.get(url, params=params, timeout=aiohttp.ClientTimeout(total=30)) as resp:
            if resp.status == 200:
                data = await resp.json()
                result = {
                    "city": city["name"],
                    "temp_c": data["main"]["temp"],
                    "humidity": data["main"]["humidity"],
                    "description": data["weather"][0]["description"],
                    "wind_speed": data["wind"]["speed"],
                    "fetched_at": datetime.now(timezone.utc).isoformat(),
                }
                cache.set(city["name"], result)
                return result
            else:
                logger.error(f"API error for {city['name']}: HTTP {resp.status}")
                return {"city": city["name"], "error": f"HTTP {resp.status}"}
    except asyncio.TimeoutError:
        logger.error(f"Timeout fetching weather for {city['name']}")
        return {"city": city["name"], "error": "timeout"}


async def handle_weather(request):
    """GET /weather - Return current weather for all cities."""
    config = request.app["config"]
    api_key = os.environ.get("WEATHER_API_KEY", "")

    async with aiohttp.ClientSession() as session:
        tasks = [fetch_weather(session, city, api_key) for city in config["cities"]]
        results = await asyncio.gather(*tasks)

    return web.json_response({"data": results, "count": len(results)})


async def handle_health(request):
    """GET /health - Health check endpoint."""
    return web.json_response({"status": "healthy", "service": "weather-bot", "uptime": "ok"})


def create_app(config: dict) -> web.Application:
    app = web.Application()
    app["config"] = config
    app.router.add_get("/weather", handle_weather)
    app.router.add_get("/health", handle_health)
    return app


def main():
    config = load_config(CONFIG_PATH)

    logging.basicConfig(
        level=getattr(logging, config.get("logging", {}).get("level", "INFO")),
        format="%(asctime)s [%(name)s] %(levelname)s: %(message)s",
    )

    logger.info(f"Starting Weather Bot on port {config['server']['port']}")
    logger.info(f"Monitoring {len(config['cities'])} cities")

    app = create_app(config)
    web.run_app(app, host=config["server"]["host"], port=config["server"]["port"])


if __name__ == "__main__":
    main()
