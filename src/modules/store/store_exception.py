from starlette import status
from starlette.exceptions import HTTPException


class StoreInvalidNameException(HTTPException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY

    def __init__(self, name: str) -> None:
        detail = f'Invalid Store Name: {name}'
        super().__init__(self.status_code, detail=detail)


class StoreInvalidLocationException(HTTPException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY

    def __init__(self, location: str) -> None:
        detail = f'Invalid Store Location: {location}'
        super().__init__(self.status_code, detail=detail)


class StoreInvalidDescriptionException(HTTPException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY

    def __init__(self, description: str) -> None:
        detail = f'Invalid Store Description: {description}'
        super().__init__(self.status_code, detail=detail)


class StoreInvalidImageUrlException(HTTPException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY

    def __init__(self, image_url: str) -> None:
        detail = f'Invalid Store Image URL: {image_url}'
        super().__init__(self.status_code, detail=detail)


class StoreNotFoundException(HTTPException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = 'The store you specified does not exist.'

    def __init__(self) -> None:
        super().__init__(self.status_code, detail=self.detail)

    def __str__(self) -> str:
        return self.detail


class StoresNotFoundException(HTTPException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = 'No stores were found.'

    def __init__(self) -> None:
        super().__init__(self.status_code, detail=self.detail)

    def __str__(self) -> str:
        return self.detail
