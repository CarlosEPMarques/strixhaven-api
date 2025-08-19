from starlette import status
from starlette.exceptions import HTTPException


class NPCNoteInvalidNoteIdException(HTTPException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY

    def __init__(self, note_id: str) -> None:
        detail = f'Invalid Note ID: {note_id}'
        super().__init__(self.status_code, detail=detail)


class NPCNoteInvalidNPCIdException(HTTPException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY

    def __init__(self, npc_id: str) -> None:
        detail = f'Invalid NPC ID: {npc_id}'
        super().__init__(self.status_code, detail=detail)


class NPCNoteInvalidAuthorIdException(HTTPException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY

    def __init__(self, author_id: str) -> None:
        detail = f'Invalid Author ID: {author_id}'
        super().__init__(self.status_code, detail=detail)


class NPCNoteNotFoundException(HTTPException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = 'The NPC note you specified does not exist.'

    def __init__(self) -> None:
        super().__init__(self.status_code, detail=self.detail)

    def __str__(self) -> str:
        return self.detail


class NPCNotesNotFoundException(HTTPException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = 'No NPC notes were found.'

    def __init__(self) -> None:
        super().__init__(self.status_code, detail=self.detail)

    def __str__(self) -> str:
        return self.detail
