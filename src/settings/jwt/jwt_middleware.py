from fastapi import Request
from src.settings.jwt.jwt_exception import JWTTokenInvalidException, JWTTokenMissingException
from src.settings.jwt.jwt_service import verify_token

async def jwt_middleware(request: Request, call_next):
    if request.url.path.startswith("/login") or request.url.path.startswith("/docs"):
        return await call_next(request)
    
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        raise JWTTokenMissingException()
    
    token = auth_header.split(" ")[1]
    try:
        user_data = verify_token(token)
        request.state.user = user_data
    except JWTTokenInvalidException:
        raise
    return await call_next(request)

