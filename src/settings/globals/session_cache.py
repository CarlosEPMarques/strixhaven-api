from cachetools import TTLCache
from src.settings.jwt import jwt_settings

session_cache = TTLCache(
    maxsize=jwt_settings.SESSION_MAX,
    ttl=jwt_settings.SESSION_TTL
)
