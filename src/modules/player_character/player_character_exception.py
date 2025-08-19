from starlette import status
from starlette.exceptions import HTTPException


class PlayerCharacterInvalidUserIdException(HTTPException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY

    def __init__(self, user_id: str) -> None:
        detail = f'Invalid User ID: {user_id}'
        super().__init__(self.status_code, detail=detail)


class PlayerCharacterInvalidNameException(HTTPException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY

    def __init__(self, name: str) -> None:
        detail = f'Invalid Name: {name}'
        super().__init__(self.status_code, detail=detail)


class PlayerCharacterInvalidImageUrlException(HTTPException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY

    def __init__(self, image_url: str) -> None:
        detail = f'Invalid Image URL: {image_url}'
        super().__init__(self.status_code, detail=detail)


class PlayerCharacterInvalidCollegeYearException(HTTPException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY

    def __init__(self, college_year: str) -> None:
        detail = f'Invalid College Year: {college_year}'
        super().__init__(self.status_code, detail=detail)


class PlayerCharacterInvalidCollegeIdException(HTTPException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY

    def __init__(self, college_id: str) -> None:
        detail = f'Invalid College ID: {college_id}'
        super().__init__(self.status_code, detail=detail)


class PlayerCharacterInvalidEnrolledClassesException(HTTPException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY

    def __init__(self, enrolled_classes: str) -> None:
        detail = f'Invalid Enrolled Classes: {enrolled_classes}'
        super().__init__(self.status_code, detail=detail)


class PlayerCharacterInvalidLevelException(HTTPException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY

    def __init__(self, level: str) -> None:
        detail = f'Invalid Level: {level}'
        super().__init__(self.status_code, detail=detail)


class PlayerCharacterNotFoundException(HTTPException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = 'The player character you specified does not exist.'

    def __init__(self) -> None:
        super().__init__(self.status_code, detail=self.detail)

    def __str__(self) -> str:
        return self.detail


class PlayerCharactersNotFoundException(HTTPException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = 'No player characters were found.'

    def __init__(self) -> None:
        super().__init__(self.status_code, detail=self.detail)

    def __str__(self) -> str:
        return self.detail
