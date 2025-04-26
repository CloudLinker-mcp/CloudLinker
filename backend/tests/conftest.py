import os
import sys
import pytest

# Add the backend directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Set test environment file
os.environ["ENV_FILE"] = os.path.join(os.path.dirname(__file__), ".env.test")

from src.settings import settings

@pytest.fixture(autouse=True)
def _patch_api_keys(monkeypatch):
    """Force tests to have a known key."""
    monkeypatch.setattr(settings, "api_keys", "test_key")