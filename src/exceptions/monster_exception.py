from starlette import status
from starlette.exceptions import HTTPException

class MonsterInvalidNameException(HTTPException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY

    def __init__(self, name: int):
        detail = f'Invalid Name: {name}'
        super().__init__(self.status_code, detail=detail)

class MonsterInvalidHitPointsException(HTTPException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY

    def __init__(self, hit_points: int):
        detail = f'Invalid Hit Points: {hit_points}'
        super().__init__(self.status_code, detail=detail)

class MonsterInvalidExperiencePointsException(HTTPException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY

    def __init__(self, experience_points: int):
        detail = f'Invalid Experience Points: {experience_points}'
        super().__init__(self.status_code, detail=detail)

class MonsterInvalidStrengthException(HTTPException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY

    def __init__(self, strength: int):
        detail = f'Invalid Strength: {strength}'
        super().__init__(self.status_code, detail=detail)

class MonsterInvalidDexterityException(HTTPException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY

    def __init__(self, dexterity: int):
        detail = f'Invalid Dexterity: {dexterity}'
        super().__init__(self.status_code, detail=detail)

class MonsterInvalidConstitutionException(HTTPException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY

    def __init__(self, constitution: int):
        detail = f'Invalid Constitution: {constitution}'
        super().__init__(self.status_code, detail=detail)

class MonsterInvalidIntelligenceException(HTTPException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY

    def __init__(self, intelligence: int):
        detail = f'Invalid Intelligence: {intelligence}'
        super().__init__(self.status_code, detail=detail)

class MonsterInvalidWisdomException(HTTPException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY

    def __init__(self, wisdom: int):
        detail = f'Invalid Wisdom: {wisdom}'
        super().__init__(self.status_code, detail=detail)

class MonsterInvalidCharismaException(HTTPException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY

    def __init__(self, charisma: int):
        detail = f'Invalid Charisma: {charisma}'
        super().__init__(self.status_code, detail=detail)

class MonsterInvalidArmorClassException(HTTPException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY

    def __init__(self, armor_class: int):
        detail = f'Invalid Armor Class: {armor_class}'
        super().__init__(self.status_code, detail=detail)

class MonsterInvalidDescriptionException(HTTPException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY

    def __init__(self, description: int):
        detail = f'Invalid Description: {description}'
        super().__init__(self.status_code, detail=detail)

class MonsterInvalidImageUrlException(HTTPException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY

    def __init__(self, image_url: int):
        detail = f'Invalid Image URL: {image_url}'
        super().__init__(self.status_code, detail=detail)

class MonsterNotFoundException(HTTPException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = 'The monster you specified does not exist.'
    
    def __init__(self):
        super().__init__(self.status_code, detail=self.detail)

    def __str__(self) -> str:
        return self.detail

class MonstersNotFoundException(HTTPException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = 'No monsters were found.'

    def __init__(self) -> None:
        super().__init__(status_code=self.status_code, detail=self.detail)

    def __str__(self) -> str:
        return self.detail