"""
A zero-dependency AWS Lambda function that serves
• a simple HTML docs page
• JSON data at /data
• individual records at /<id>

To deploy, zip this file together with:
  - template.html   (pure HTML/CSS, uses {environment} etc. tokens)
  - data.json       (array of dicts, optional – see fallback below)

Set the handler to `index.handler`.
"""

import json
import os
from pathlib import Path

# ---------------------------------------------------------------------------
# One-time cold-start initialisation
# ---------------------------------------------------------------------------

TEMPLATE = Path(__file__).with_name("template.html").read_text(encoding="utf-8")

try:
    DATA = json.loads(Path(__file__).with_name("data.json").read_text(encoding="utf-8"))
except FileNotFoundError:
    # Fallback sample data so the function still works if data.json is absent
    DATA = [
        {"id": "1", "name": "sample-item-1"},
        {"id": "2", "name": "sample-item-2"},
    ]

# Pre-computed headers
HTML_HEADERS = {"Content-Type": "text/html; charset=utf-8"}
JSON_HEADERS = {"Content-Type": "application/json"}


# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------


def _html_response(body: str, status: int = 200):
    return {"statusCode": status, "headers": HTML_HEADERS, "body": body}


def _json_response(obj, status: int = 200):
    return {"statusCode": status, "headers": JSON_HEADERS, "body": json.dumps(obj)}


def _inject_template_vars(html: str) -> str:
    """Replace the four {token}s in template.html with env-var values."""
    replacements = {
        "{environment}": os.getenv("ENVIRONMENT", "undefined"),
        "{version}": os.getenv("VERSION", "undefined"),
        "{build_tag}": os.getenv("BUILD_TAG", "undefined"),
        "{build_number}": os.getenv("BUILD_NUMBER", "undefined"),
    }
    for token, value in replacements.items():
        html = html.replace(token, value)
    return html


# ---------------------------------------------------------------------------
# Lambda entry point
# ---------------------------------------------------------------------------


def handler(event, _context):
    """
    Lambda handler for an HTTP API (payload format 2.0).
    Routes:
      • GET /           → HTML docs page
      • GET /data       → entire JSON list
      • GET /<id>       → single item
    """
    path = event.get("rawPath", "/")
    method = event.get("requestContext", {}).get("http", {}).get("method", "GET")

    if method != "GET":
        return _json_response({"message": "Method not allowed"}, 405)

    # ------------------------------------------------------------------ #
    #  GET /
    # ------------------------------------------------------------------ #
    if path == "/":
        page = _inject_template_vars(TEMPLATE)
        return _html_response(page)

    # ------------------------------------------------------------------ #
    #  GET /data  → full list
    # ------------------------------------------------------------------ #
    if path == "/data":
        return _json_response(DATA)

    # ------------------------------------------------------------------ #
    #  GET /<id>  → single record
    # ------------------------------------------------------------------ #
    item_id = path.lstrip("/")
    for item in DATA:
        if item["id"] == item_id:
            return _json_response(item)

    return _json_response({"message": f"item_id '{item_id}' not found"}, 404)


# ---------------------------------------------------------------------------
# Optional local test harness
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    fake_event = {
        "rawPath": "/1",
        "requestContext": {"http": {"method": "GET"}},
    }
    print(json.dumps(handler(fake_event, None), indent=2))
