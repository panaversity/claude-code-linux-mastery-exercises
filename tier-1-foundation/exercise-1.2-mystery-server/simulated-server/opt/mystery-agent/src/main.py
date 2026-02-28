#!/usr/bin/env python3
"""Weather Alert Agent - checks weather API and sends Slack notifications."""
import os
import requests
import json
from datetime import datetime

API_KEY = os.environ.get("WEATHER_API_KEY")
SLACK_WEBHOOK = os.environ.get("SLACK_WEBHOOK_URL")
CITIES = ["New York", "London", "Tokyo"]

def check_weather():
    for city in CITIES:
        resp = requests.get(f"https://api.weather.example.com/v1/alerts?city={city}&key={API_KEY}")
        alerts = resp.json().get("alerts", [])
        for alert in alerts:
            send_slack_alert(city, alert)

def send_slack_alert(city, alert):
    payload = {"text": f"⚠️ Weather Alert for {city}: {alert['description']}"}
    requests.post(SLACK_WEBHOOK, json=payload)

if __name__ == "__main__":
    print(f"[{datetime.now()}] Starting weather check...")
    check_weather()
    print(f"[{datetime.now()}] Weather check complete.")
