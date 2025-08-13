import time
import uuid
from jose import jwt, JWTError
from settings.jwt.jwt_exception import (
    JWTTokenInvalidException,
    JWTSessionInvalidException,
    JWTTokenCreationException
)

from globals.session_cache import session_cache
from src.settings.jwt.jwt_settings import jwt_settings

def create_session(user_data: dict) -> str:
    try:
        session_id = str(uuid.uuid4())
        session_cache[session_id] = user_data
        payload = {"sid": session_id, "exp": time.time() + jwt_settings.SESSION_TTL}
        return jwt.encode(payload, jwt_settings.SECRET_KEY, algorithm=jwt_settings.ALGORITHM)
    except Exception:
        raise JWTTokenCreationException()

def verify_token(token: str) -> dict:
    try:
        payload = jwt.decode(token, jwt_settings.SECRET_KEY, algorithms=[jwt_settings.ALGORITHM])
        sid = payload.get("sid")
        if not sid or sid not in session_cache:
            raise JWTSessionInvalidException()
        return session_cache[sid]
    except JWTError:
        raise JWTTokenInvalidException()

def logout_session(session_id: str):
    session_cache.pop(session_id, None)
