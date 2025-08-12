from starlette import status
from starlette.exceptions import HTTPException

class EventNoteInvalidNoteIdException(HTTPException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY

    def __init__(self, note_id: str):
        detail = f'Invalid Note ID: {note_id}'
        super().__init__(self.status_code, detail=detail)

class EventNoteInvalidEventIdException(HTTPException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY

    def __init__(self, event_id: str):
        detail = f'Invalid Event ID: {event_id}'
        super().__init__(self.status_code, detail=detail)

class EventNoteInvalidAuthorIdException(HTTPException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY

    def __init__(self, author_id: str):
        detail = f'Invalid Author ID: {author_id}'
        super().__init__(self.status_code, detail=detail)

class EventNoteNotFoundException(HTTPException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = 'The event note you specified does not exist.'
    
    def __init__(self):
        super().__init__(self.status_code, detail=self.detail)

    def __str__(self) -> str:
        return self.detail

class EventNotesNotFoundException(HTTPException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = 'No event notes were found.'

    def __init__(self) -> None:
        super().__init__(status_code=self.status_code, detail=self.detail)

    def __str__(self) -> str:
        return self.detail