from starlette import status
from starlette.exceptions import HTTPException


class ClassInvalidNameException(HTTPException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY

    def __init__(self, name: str) -> None:
        detail = f'Invalid Name: {name}'
        super().__init__(self.status_code, detail=detail)


class ClassInvalidDescriptionException(HTTPException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY

    def __init__(self, description: str) -> None:
        detail = f'Invalid Description: {description}'
        super().__init__(self.status_code, detail=detail)


class ClassInvalidCollegeIdException(HTTPException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY

    def __init__(self, college_id: str) -> None:
        detail = f'Invalid College ID: {college_id}'
        super().__init__(self.status_code, detail=detail)


class ClassInvalidImageUrlException(HTTPException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY

    def __init__(self, image_url: str) -> None:
        detail = f'Invalid Image URL: {image_url}'
        super().__init__(self.status_code, detail=detail)


class ClassNotFoundException(HTTPException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = 'The class you specified does not exist.'

    def __init__(self) -> None:
        super().__init__(self.status_code, detail=self.detail)

    def __str__(self) -> str:
        return self.detail


class ClassesNotFoundException(HTTPException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = 'No classes were found.'

    def __init__(self) -> None:
        super().__init__(status_code=self.status_code, detail=self.detail)

    def __str__(self) -> str:
        return self.detail

class ClassAlreadyExistsException(HTTPException):
    status_code = status.HTTP_409_CONFLICT
    
    def __init__(self, class_name: str):
        detail = f'Class with name {class_name} already exists.'
        super().__init__(status_code=self.status_code, detail=detail)
    
    def __str__(self) -> str:
        return self.detail