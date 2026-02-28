#!/usr/bin/env python3
"""Data Collector Agent - collects product data from APIs."""
import os
import json
import logging

# BUG: logs/ directory doesn't exist, this will crash
logging.basicConfig(filename='logs/collector.log', level=logging.INFO)

def collect_data():
    api_key = os.environ.get("API_KEY")
    logging.info("Starting data collection...")
    # ... collection logic ...
    logging.info("Collection complete.")

if __name__ == "__main__":
    collect_data()
