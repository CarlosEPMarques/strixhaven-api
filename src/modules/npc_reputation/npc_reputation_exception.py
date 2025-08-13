from starlette import status
from starlette.exceptions import HTTPException

class NPCReputationInvalidCharacterIdException(HTTPException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY

    def __init__(self, character_id: str):
        detail = f'Invalid Character ID: {character_id}'
        super().__init__(self.status_code, detail=detail)

class NPCReputationInvalidNPCIdException(HTTPException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY

    def __init__(self, npc_id: str):
        detail = f'Invalid NPC ID: {npc_id}'
        super().__init__(self.status_code, detail=detail)

class NPCReputationInvalidScoreException(HTTPException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY

    def __init__(self, score: str):
        detail = f'Invalid Score: {score}'
        super().__init__(self.status_code, detail=detail)

class NPCReputationNotFoundException(HTTPException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = 'The NPC reputation you specified does not exist.'
    
    def __init__(self):
        super().__init__(self.status_code, detail=self.detail)

    def __str__(self) -> str:
        return self.detail

class NPCReputationsNotFoundException(HTTPException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = 'No NPC reputations were found.'

    def __init__(self):
        super().__init__(self.status_code, detail=self.detail)

    def __str__(self) -> str:
        return self.detail
