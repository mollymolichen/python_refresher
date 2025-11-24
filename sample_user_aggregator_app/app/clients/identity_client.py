# app/clients/identity_client.py
import requests                 # REST client
from typing import Optional

class IdentityClient:
    def __init__(self, base_url: str, timeout_seconds: float = 2.0):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout_seconds  # design mentioned timeouts

    def fetch_identity(self, user_id: str, auth_token: Optional[str] = None) -> dict:
        """
        Fetch identity data via REST. This implementation is strict:
        - uses a timeout
        - raises for non-200 responses (matches the original design's lack of graceful failure)
        """
        url = f"{self.base_url}/v1/identities/{user_id}"
        headers = {}
        if auth_token:
            headers["Authorization"] = f"Bearer {auth_token}"

        resp = requests.get(url, headers=headers, timeout=self.timeout)
        # Original design: no graceful handling of non-success -> raise
        resp.raise_for_status()
        return resp.json()
