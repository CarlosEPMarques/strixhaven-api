from typing import Any

from cachetools import TTLCache

from src.settings.jwt.jwt_settings import jwt_settings

session_cache: TTLCache[str, Any] = TTLCache(
    maxsize=jwt_settings.SESSION_MAX, ttl=jwt_settings.SESSION_TTL
)
