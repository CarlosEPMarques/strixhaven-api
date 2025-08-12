from starlette import status
from starlette.exceptions import HTTPException

class NPCInvalidNameException(HTTPException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY

    def __init__(self, name: str):
        detail = f'Invalid Name: {name}'
        super().__init__(self.status_code, detail=detail)

class NPCInvalidImageUrlException(HTTPException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY

    def __init__(self, image_url: str):
        detail = f'Invalid Image URL: {image_url}'
        super().__init__(self.status_code, detail=detail)

class NPCInvalidBioException(HTTPException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY

    def __init__(self, bio: str):
        detail = f'Invalid Bio: {bio}'
        super().__init__(self.status_code, detail=detail)

class NPCInvalidVisibleToException(HTTPException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY

    def __init__(self, visible_to: str):
        detail = f'Invalid Visible To: {visible_to}'
        super().__init__(self.status_code, detail=detail)

class NPCNotFoundException(HTTPException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = 'The NPC you specified does not exist.'
    
    def __init__(self):
        super().__init__(self.status_code, detail=self.detail)

    def __str__(self) -> str:
        return self.detail

class NPCsNotFoundException(HTTPException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = 'No NPCs were found.'

    def __init__(self):
        super().__init__(self.status_code, detail=self.detail)

    def __str__(self) -> str:
        return self.detail
