from starlette import status
from starlette.exceptions import HTTPException

class MapInvalidTitleException(HTTPException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY

    def __init__(self, title: str):
        detail = f'Invalid Title: {title}'
        super().__init__(self.status_code, detail=detail)

class MapInvalidImageUrlException(HTTPException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY

    def __init__(self, image_url: str):
        detail = f'Invalid Image URL: {image_url}'
        super().__init__(self.status_code, detail=detail)

class MapNotFoundException(HTTPException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = 'The map you specified does not exist.'
    
    def __init__(self):
        super().__init__(self.status_code, detail=self.detail)

    def __str__(self) -> str:
        return self.detail

class MapsNotFoundException(HTTPException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = 'No maps were found.'

    def __init__(self) -> None:
        super().__init__(status_code=self.status_code, detail=self.detail)

    def __str__(self) -> str:
        return self.detail