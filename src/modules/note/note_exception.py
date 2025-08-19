from starlette import status
from starlette.exceptions import HTTPException


class NoteInvalidAuthorIdException(HTTPException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY

    def __init__(self, author_id: str) -> None:
        detail = f'Invalid Author ID: {author_id}'
        super().__init__(self.status_code, detail=detail)


class NoteInvalidContentException(HTTPException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY

    def __init__(self, content: str) -> None:
        detail = f'Invalid Content: {content}'
        super().__init__(self.status_code, detail=detail)


class NoteNotFoundException(HTTPException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = 'The note you specified does not exist.'

    def __init__(self) -> None:
        super().__init__(self.status_code, detail=self.detail)

    def __str__(self) -> str:
        return self.detail


class NotesNotFoundException(HTTPException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = 'No notes were found.'

    def __init__(self) -> None:
        super().__init__(self.status_code, detail=self.detail)

    def __str__(self) -> str:
        return self.detail
