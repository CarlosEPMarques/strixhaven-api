from datetime import datetime
from starlette import status
from starlette.exceptions import HTTPException

class NewsInvalidHeadlineException(HTTPException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY

    def __init__(self, headline: str):
        detail = f'Invalid Headline: {headline}'
        super().__init__(self.status_code, detail=detail)

class NewsInvalidBodyException(HTTPException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY

    def __init__(self, body: str):
        detail = f'Invalid Body: {body}'
        super().__init__(self.status_code, detail=detail)

class NewsInvalidDatetimeException(HTTPException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY

    def __init__(self, datetime: datetime):
        detail = f'Invalid Datetime: {datetime}'
        super().__init__(self.status_code, detail=detail)

class NewsInvalidImageUrlException(HTTPException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY

    def __init__(self, image_url: str):
        detail = f'Invalid Image URL: {image_url}'
        super().__init__(self.status_code, detail=detail)

class SingleNewsNotFoundException(HTTPException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = 'The news you specified does not exist.'
    
    def __init__(self):
        super().__init__(self.status_code, detail=self.detail)

    def __str__(self) -> str:
        return self.detail

class AllNewsNotFoundException(HTTPException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = 'No news were found.'

    def __init__(self):
        super().__init__(self.status_code, detail=self.detail)

    def __str__(self) -> str:
        return self.detail
