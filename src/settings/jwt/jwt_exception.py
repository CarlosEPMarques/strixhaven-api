from starlette import status
from starlette.exceptions import HTTPException


class JWTTokenMissingException(HTTPException):
    status_code = status.HTTP_403_FORBIDDEN

    def __init__(self):
        detail = "Authorization token is missing."
        super().__init__(self.status_code, detail=detail)


class JWTTokenInvalidException(HTTPException):
    status_code = status.HTTP_403_FORBIDDEN

    def __init__(self):
        detail = "Authorization token is invalid."
        super().__init__(self.status_code, detail=detail)


class JWTSessionInvalidException(HTTPException):
    status_code = status.HTTP_403_FORBIDDEN

    def __init__(self):
        detail = "User session is invalid or has expired."
        super().__init__(self.status_code, detail=detail)


class JWTTokenCreationException(HTTPException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR

    def __init__(self):
        detail = "Failed to create authorization token."
        super().__init__(self.status_code, detail=detail)
