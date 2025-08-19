from fastapi import Response
from starlette.middleware.base import RequestResponseEndpoint
from starlette.requests import Request

from src.settings.jwt.jwt_exception import JWTTokenMissingException
from src.settings.jwt.jwt_service import verify_token

PUBLIC_PATHS = {'/', '/login', '/signup', '/docs', '/openapi.json', '/favicon.ico'}


async def jwt_middleware(request: Request, call_next: RequestResponseEndpoint) -> Response:
    if request.url.path in PUBLIC_PATHS:
        return await call_next(request)

    auth_header = request.headers.get('Authorization')
    if not auth_header or not auth_header.startswith('Bearer '):
        raise JWTTokenMissingException

    token = auth_header.split(' ')[1]
    user_data = verify_token(token)
    request.state.user = user_data
    return await call_next(request)
