from __future__ import annotations

import os
from typing import Any, Dict

from dotenv import load_dotenv
import yaml


def load_env() -> None:
    """Load environment variables from a local .env file if present."""
    load_dotenv()


def load_config(path: str = "config/config.yaml") -> Dict[str, Any]:
    """Load YAML config into a Python dict.

    Keep it minimal: no validation here, just parsing.
    """
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def load_profile(path: str = "config/profile.yaml") -> Dict[str, Any]:
    """Load profile YAML into a Python dict."""
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}
