# app/clients/contacts_client.py
import requests
from typing import Optional

class ContactsClient:
    def __init__(self, base_url: str, timeout_seconds: float = 2.0):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout_seconds

    def fetch_contacts(self, user_id: str, auth_token: Optional[str] = None) -> dict:
        """
        Fetch contact-like info. Original design passes auth token to downstream services.
        Returns JSON response; raises on non-200 status (original design behavior).
        """
        url = f"{self.base_url}/v1/users/{user_id}/contacts"
        headers = {}
        if auth_token:
            headers["Authorization"] = f"Bearer {auth_token}"
        resp = requests.get(url, headers=headers, timeout=self.timeout)
        resp.raise_for_status()
        return resp.json()
