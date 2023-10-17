from typing import Any
import aiohttp

from .plisio_exceptions import PlisioError


class _BaseAIOPlisioClient:
    _BASE_API_URL: str = "https://plisio.net/api/v1"

    def __init__(self, api_key: str) -> None:
        self._api_key = api_key

    async def __aenter__(self):
        return self
    
    async def __aexit__(self, exc_type, exc_value, traceback):
        return None
    
    async def _make_request(self, endpoint: str, post: bool=False, **kwargs) -> Any:
        async with aiohttp.ClientSession() as session:
            response = await session.get(f"{self._BASE_API_URL}/{endpoint}", **kwargs)
            if post:
                response = await session.post(f"{self._BASE_API_URL}/{endpoint}", **kwargs)
            data = await response.json()

            if "status" in data and data["status"] == "error":
                error_message, error_code = data["data"]["message"], data["data"]["code"]
                raise PlisioError(error_message, error_code)
            return data