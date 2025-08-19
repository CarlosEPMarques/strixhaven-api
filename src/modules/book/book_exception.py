from starlette import status
from starlette.exceptions import HTTPException

class BookInvalidTitleException(HTTPException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY

    def __init__(self, title: str):
        detail = f'Invalid Title: {title}'
        super().__init__(self.status_code, detail=detail)

class BookInvalidSummaryException(HTTPException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY

    def __init__(self, summary: str):
        detail = f'Invalid Summary: {summary}'
        super().__init__(self.status_code, detail=detail)

class BookInvalidSectionException(HTTPException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY

    def __init__(self, section: str):
        detail = f'Invalid Section: {section}'
        super().__init__(self.status_code, detail=detail)

class BookInvalidIsHiddenException(HTTPException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY

    def __init__(self, is_hidden: str):
        detail = f'Invalid Is Hidden: {is_hidden}'
        super().__init__(self.status_code, detail=detail)

class BookInvalidImageUrlException(HTTPException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY

    def __init__(self, image_url: str):
        detail = f'Invalid Image URL: {image_url}'
        super().__init__(self.status_code, detail=detail)

class BookNotFoundException(HTTPException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = 'The book you specified does not exist.'
    
    def __init__(self):
        super().__init__(self.status_code, detail=self.detail)

    def __str__(self) -> str:
        return self.detail

class BooksNotFoundException(HTTPException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = 'No books were found.'

    def __init__(self) -> None:
        super().__init__(status_code=self.status_code, detail=self.detail)

    def __str__(self) -> str:
        return self.detail