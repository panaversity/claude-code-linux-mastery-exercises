#!/usr/bin/env python3
"""Social Media Monitor Agent - tracks brand mentions across platforms."""
import os
import time
import logging

logging.basicConfig(
    filename=os.path.join(os.path.dirname(__file__), '..', 'logs', 'monitor.log'),
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s'
)

def monitor_mentions():
    api_key = os.environ.get("SOCIAL_API_KEY")
    if not api_key:
        logging.error("SOCIAL_API_KEY not set!")
        raise SystemExit(1)
    
    logging.info("Starting social media monitoring...")
    while True:
        # Check mentions every 5 minutes
        logging.info("Checking brand mentions...")
        time.sleep(300)

if __name__ == "__main__":
    monitor_mentions()
