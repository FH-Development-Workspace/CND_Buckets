import os

import httpx
from dotenv import load_dotenv


load_dotenv()

FH_API_URL = os.getenv("FH_API_URL")
FH_API_KEY = os.getenv("FH_API_KEY")


if not FH_API_URL:
    raise RuntimeError("FH_API_URL is missing from .env")

if not FH_API_KEY:
    raise RuntimeError("FH_API_KEY is missing from .env")


class FHAPIError(Exception):
    def __init__(self, status_code: int, detail):
        self.status_code = status_code
        self.detail = detail

        super().__init__(
            f"FH API returned {status_code}: {detail}"
        )


async def create_license(
    discord_id: str,
    roblox_id: str,
    product_id: str,
    expires_at: str | None = None,
    file_id: int | None = None,
):
    payload = {
        "discord_id": discord_id,
        "roblox_id": roblox_id,
        "product_id": product_id,
        "expires_at": expires_at,
        "file_id": file_id,
    }

    headers = {
        "X-API-Key": FH_API_KEY,
    }

    async with httpx.AsyncClient(
        timeout=30.0
    ) as client:
        response = await client.post(
            f"{FH_API_URL}/licenses",
            json=payload,
            headers=headers,
        )

    if response.status_code >= 400:
        try:
            detail = response.json()
        except Exception:
            detail = response.text

        raise FHAPIError(
            response.status_code,
            detail,
        )

    return response.json()
