#!/usr/bin/env python3
"""
Data Processor - Batch data pipeline agent.

Reads CSV files from the input directory, processes them through
configurable pipeline stages, and writes results to the output directory.

Runs as a oneshot systemd service triggered by a timer.

Usage:
    python3 processor.py --config /etc/data-processor/pipeline.yaml
"""

import os
import sys
import csv
import json
import yaml
import logging
import argparse
from datetime import datetime, timezone
from pathlib import Path

logger = logging.getLogger("data-processor")

DEFAULT_CONFIG = "/etc/data-processor/pipeline.yaml"


def load_config(path: str) -> dict:
    with open(path, "r") as f:
        return yaml.safe_load(f)


def discover_input_files(input_dir: str) -> list[Path]:
    """Find all pending CSV files in the input directory."""
    input_path = Path(input_dir)
    if not input_path.exists():
        logger.warning(f"Input directory does not exist: {input_dir}")
        return []

    files = sorted(input_path.glob("*.csv"))
    logger.info(f"Found {len(files)} input files in {input_dir}")
    return files


def process_batch(filepath: Path, config: dict) -> list[dict]:
    """Process a single CSV file through the pipeline."""
    results = []
    batch_size = config.get("pipeline", {}).get("batch_size", 100)

    with open(filepath, "r") as f:
        reader = csv.DictReader(f)
        batch = []

        for row in reader:
            batch.append(row)

            if len(batch) >= batch_size:
                processed = transform_batch(batch, config)
                results.extend(processed)
                batch = []

        # Process remaining
        if batch:
            processed = transform_batch(batch, config)
            results.extend(processed)

    logger.info(f"Processed {len(results)} records from {filepath.name}")
    return results


def transform_batch(batch: list[dict], config: dict) -> list[dict]:
    """Apply transformations to a batch of records."""
    transformed = []
    for record in batch:
        result = {
            "id": record.get("id", "unknown"),
            "processed_at": datetime.now(timezone.utc).isoformat(),
            "source": record,
            "status": "processed",
        }
        transformed.append(result)
    return transformed


def write_output(results: list[dict], output_dir: str):
    """Write processed results to the output directory."""
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    output_file = output_path / f"processed-{timestamp}.json"

    with open(output_file, "w") as f:
        json.dump({"records": results, "count": len(results), "timestamp": timestamp}, f, indent=2)

    logger.info(f"Wrote {len(results)} records to {output_file}")


def main():
    parser = argparse.ArgumentParser(description="Data Processor Pipeline")
    parser.add_argument("--config", default=DEFAULT_CONFIG, help="Path to pipeline config")
    args = parser.parse_args()

    config = load_config(args.config)

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(name)s] %(levelname)s: %(message)s",
    )

    logger.info("Data Processor starting batch run")
    logger.info(f"Config: {args.config}")

    input_dir = config["pipeline"]["input_dir"]
    output_dir = config["pipeline"]["output_dir"]

    files = discover_input_files(input_dir)
    if not files:
        logger.info("No input files to process. Exiting.")
        return

    all_results = []
    for filepath in files:
        results = process_batch(filepath, config)
        all_results.extend(results)

    write_output(all_results, output_dir)

    logger.info(f"Batch complete: {len(all_results)} total records processed")


if __name__ == "__main__":
    main()
