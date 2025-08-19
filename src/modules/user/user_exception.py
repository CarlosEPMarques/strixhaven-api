from starlette import status
from starlette.exceptions import HTTPException


class UserInvalidNameException(HTTPException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY

    def __init__(self, name: str) -> None:
        detail = f'Invalid User Name: {name}'
        super().__init__(self.status_code, detail=detail)


class UserInvalidEmailException(HTTPException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY

    def __init__(self, email: str) -> None:
        detail = f'Invalid User Email: {email}'
        super().__init__(self.status_code, detail=detail)


class UserInvalidPasswordException(HTTPException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY

    def __init__(self, password: str) -> None:
        detail = f'Invalid User Password: {password}'
        super().__init__(self.status_code, detail=detail)


class UserInvalidRoleException(HTTPException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY

    def __init__(self, role: str) -> None:
        detail = f'Invalid User Role: {role}'
        super().__init__(self.status_code, detail=detail)


class UserInvalidAvatarUrlException(HTTPException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY

    def __init__(self, avatar_url: str) -> None:
        detail = f'Invalid User Avatar URL: {avatar_url}'
        super().__init__(self.status_code, detail=detail)


class UserNotFoundException(HTTPException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = 'The user you specified does not exist.'

    def __init__(self) -> None:
        super().__init__(self.status_code, detail=self.detail)

    def __str__(self) -> str:
        return self.detail
