from starlette import status
from starlette.exceptions import HTTPException

class CharacterNoteInvalidNoteIdException(HTTPException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY

    def __init__(self, note_id: str):
        detail = f'Invalid Note ID: {note_id}'
        super().__init__(self.status_code, detail=detail)

class CharacterNoteInvalidCharacterIdException(HTTPException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY

    def __init__(self, character_id: str):
        detail = f'Invalid Character ID: {character_id}'
        super().__init__(self.status_code, detail=detail)


class CharacterNoteNotFoundException(HTTPException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = 'The character note you specified does not exist.'
    
    def __init__(self):
        super().__init__(self.status_code, detail=self.detail)

    def __str__(self) -> str:
        return self.detail

class CharacterNotesNotFoundException(HTTPException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = 'No character notes were found.'

    def __init__(self) -> None:
        super().__init__(status_code=self.status_code, detail=self.detail)

    def __str__(self) -> str:
        return self.detail