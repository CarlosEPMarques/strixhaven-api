from datetime import datetime

from starlette import status
from starlette.exceptions import HTTPException


class CalendarNoteInvalidTitleException(HTTPException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY

    def __init__(self, title: str) -> None:
        detail = f'Invalid Title: {title}'
        super().__init__(self.status_code, detail=detail)


class CalendarNoteInvalidDescriptionException(HTTPException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY

    def __init__(self, description: str) -> None:
        detail = f'Invalid Description: {description}'
        super().__init__(self.status_code, detail=detail)


class CalendarNoteInvalidDatetimeException(HTTPException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY

    def __init__(self, datetime: datetime) -> None:
        detail = f'Invalid Datetime: {datetime}'
        super().__init__(self.status_code, detail=detail)


class CalendarNoteNotFoundException(HTTPException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = 'The calendar note you specified does not exist.'

    def __init__(self) -> None:
        super().__init__(self.status_code, detail=self.detail)

    def __str__(self) -> str:
        return self.detail


class CalendarNotesNotFoundException(HTTPException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = 'No calendar notes were found.'

    def __init__(self) -> None:
        super().__init__(status_code=self.status_code, detail=self.detail)

    def __str__(self) -> str:
        return self.detail
