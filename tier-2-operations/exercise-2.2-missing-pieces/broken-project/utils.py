"""Utility functions for data collector."""

def parse_response(data):
    return data.get("results", [])

def format_output(results):
    return json.dumps(results, indent=2)
