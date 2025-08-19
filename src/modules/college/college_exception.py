from starlette import status
from starlette.exceptions import HTTPException


class CollegeInvalidNameException(HTTPException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY

    def __init__(self, name: str) -> None:
        detail = f'Invalid Name: {name}'
        super().__init__(self.status_code, detail=detail)


class CollegeInvalidDescriptionException(HTTPException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY

    def __init__(self, description: str) -> None:
        detail = f'Invalid Description: {description}'
        super().__init__(self.status_code, detail=detail)


class CollegeInvalidImageUrlException(HTTPException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY

    def __init__(self, image_url: str) -> None:
        detail = f'Invalid Image URL: {image_url}'
        super().__init__(self.status_code, detail=detail)


class CollegeNotFoundException(HTTPException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = 'The college you specified does not exist.'

    def __init__(self) -> None:
        super().__init__(self.status_code, detail=self.detail)

    def __str__(self) -> str:
        return self.detail


class CollegesNotFoundException(HTTPException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = 'No colleges were found.'

    def __init__(self) -> None:
        super().__init__(status_code=self.status_code, detail=self.detail)

    def __str__(self) -> str:
        return self.detail
