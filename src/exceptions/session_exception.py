from starlette import status
from starlette.exceptions import HTTPException

class SessionInvalidSessionIdException(HTTPException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY

    def __init__(self, session_id: str):
        detail = f'Invalid Session ID: {session_id}'
        super().__init__(self.status_code, detail=detail)

class SessionInvalidUserIdException(HTTPException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY

    def __init__(self, user_id: str):
        detail = f'Invalid User ID: {user_id}'
        super().__init__(self.status_code, detail=detail)

class SessionNotFoundException(HTTPException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = 'The session you specified does not exist.'
    
    def __init__(self):
        super().__init__(self.status_code, detail=self.detail)

    def __str__(self) -> str:
        return self.detail
