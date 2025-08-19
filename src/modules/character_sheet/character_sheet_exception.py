from starlette import status
from starlette.exceptions import HTTPException


class CharacterSheetInvalidStrengthException(HTTPException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY

    def __init__(self, strength: int) -> None:
        detail = f'Invalid Strength: {strength}'
        super().__init__(self.status_code, detail=detail)


class CharacterSheetInvalidDexterityException(HTTPException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY

    def __init__(self, dexterity: int) -> None:
        detail = f'Invalid Dexterity: {dexterity}'
        super().__init__(self.status_code, detail=detail)


class CharacterSheetInvalidConstitutionException(HTTPException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY

    def __init__(self, constitution: int) -> None:
        detail = f'Invalid Constitution: {constitution}'
        super().__init__(self.status_code, detail=detail)


class CharacterSheetInvalidIntelligenceException(HTTPException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY

    def __init__(self, intelligence: int) -> None:
        detail = f'Invalid Intelligence: {intelligence}'
        super().__init__(self.status_code, detail=detail)


class CharacterSheetInvalidWisdomException(HTTPException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY

    def __init__(self, wisdom: int) -> None:
        detail = f'Invalid Wisdom: {wisdom}'
        super().__init__(self.status_code, detail=detail)


class CharacterSheetInvalidCharismaException(HTTPException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY

    def __init__(self, charisma: int) -> None:
        detail = f'Invalid Charisma: {charisma}'
        super().__init__(self.status_code, detail=detail)


class CharacterSheetInvalidProficiencyBonusException(HTTPException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY

    def __init__(self, proficiency_bonus: int) -> None:
        detail = f'Invalid Proficiency Bonus: {proficiency_bonus}'
        super().__init__(self.status_code, detail=detail)


class CharacterSheetInvalidArmorClassException(HTTPException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY

    def __init__(self, armor_class: int) -> None:
        detail = f'Invalid Armor Class: {armor_class}'
        super().__init__(self.status_code, detail=detail)


class CharacterSheetInvalidInitiativeException(HTTPException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY

    def __init__(self, initiative: int) -> None:
        detail = f'Invalid Initiative: {initiative}'
        super().__init__(self.status_code, detail=detail)


class CharacterSheetInvalidSpeedException(HTTPException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY

    def __init__(self, speed: float) -> None:
        detail = f'Invalid Speed: {speed}'
        super().__init__(self.status_code, detail=detail)


class CharacterSheetInvalidMaxHitPointsException(HTTPException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY

    def __init__(self, max_hit_points: int) -> None:
        detail = f'Invalid Max Hit Points: {max_hit_points}'
        super().__init__(self.status_code, detail=detail)


class CharacterSheetInvalidCurrentHitPointsException(HTTPException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY

    def __init__(self, current_hit_points: int) -> None:
        detail = f'Invalid Current Hit Points: {current_hit_points}'
        super().__init__(self.status_code, detail=detail)


class CharacterSheetInvalidTempHitPointsException(HTTPException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY

    def __init__(self, temp_hit_points: int) -> None:
        detail = f'Invalid Temp. Hit Points: {temp_hit_points}'
        super().__init__(self.status_code, detail=detail)


class CharacterSheetInvalidHitDiceTotalException(HTTPException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY

    def __init__(self, hit_dice_total: int) -> None:
        detail = f'Invalid Hit Dice Total: {hit_dice_total}'
        super().__init__(self.status_code, detail=detail)


class CharacterSheetInvalidHitDiceCurrentException(HTTPException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY

    def __init__(self, hit_dice_current: int) -> None:
        detail = f'Invalid Hit Dice Current: {hit_dice_current}'
        super().__init__(self.status_code, detail=detail)


class CharacterSheetInvalidSaveStrengthException(HTTPException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY

    def __init__(self, save_strength: int) -> None:
        detail = f'Invalid Save Strength: {save_strength}'
        super().__init__(self.status_code, detail=detail)


class CharacterSheetInvalidSaveDexterityException(HTTPException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY

    def __init__(self, save_dexterity: int) -> None:
        detail = f'Invalid Save Dexterity: {save_dexterity}'
        super().__init__(self.status_code, detail=detail)


class CharacterSheetInvalidSaveConstitutionException(HTTPException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY

    def __init__(self, save_constitution: int) -> None:
        detail = f'Invalid Save Constitution: {save_constitution}'
        super().__init__(self.status_code, detail=detail)


class CharacterSheetInvalidSaveIntelligenceException(HTTPException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY

    def __init__(self, save_intelligence: int) -> None:
        detail = f'Invalid Save Intelligence: {save_intelligence}'
        super().__init__(self.status_code, detail=detail)


class CharacterSheetInvalidSaveWisdomException(HTTPException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY

    def __init__(self, save_wisdom: int) -> None:
        detail = f'Invalid Save Wisdom: {save_wisdom}'
        super().__init__(self.status_code, detail=detail)


class CharacterSheetInvalidSaveCharismaException(HTTPException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY

    def __init__(self, save_charisma: int) -> None:
        detail = f'Invalid Save Charisma: {save_charisma}'
        super().__init__(self.status_code, detail=detail)


class CharacterSheetInvalidSkillsException(HTTPException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY

    def __init__(self, skills: str) -> None:
        detail = f'Invalid Skills: {skills}'
        super().__init__(self.status_code, detail=detail)


class CharacterSheetInvalidBackgroundException(HTTPException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY

    def __init__(self, background: str) -> None:
        detail = f'Invalid Background: {background}'
        super().__init__(self.status_code, detail=detail)


class CharacterSheetInvalidRaceException(HTTPException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY

    def __init__(self, race: str) -> None:
        detail = f'Invalid Race: {race}'
        super().__init__(self.status_code, detail=detail)


class CharacterSheetInvalidAlignmentException(HTTPException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY

    def __init__(self, alignment: str) -> None:
        detail = f'Invalid Alignment: {alignment}'
        super().__init__(self.status_code, detail=detail)


class CharacterSheetInvalidExperiencePointsException(HTTPException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY

    def __init__(self, experience_points: int) -> None:
        detail = f'Invalid Experience Points: {experience_points}'
        super().__init__(self.status_code, detail=detail)


class CharacterSheetInvalidLanguagesException(HTTPException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY

    def __init__(self, languages: str) -> None:
        detail = f'Invalid Languages: {languages}'
        super().__init__(self.status_code, detail=detail)


class CharacterSheetInvalidFeaturesTraitsException(HTTPException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY

    def __init__(self, features_traits: str) -> None:
        detail = f'Invalid Features Traits: {features_traits}'
        super().__init__(self.status_code, detail=detail)


class CharacterSheetInvalidProficienciesException(HTTPException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY

    def __init__(self, proficiencies: str) -> None:
        detail = f'Invalid Proficiencies: {proficiencies}'
        super().__init__(self.status_code, detail=detail)


class CharacterSheetInvalidDescriptionException(HTTPException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY

    def __init__(self, description: str) -> None:
        detail = f'Invalid Description: {description}'
        super().__init__(self.status_code, detail=detail)


class CharacterSheetNotFoundException(HTTPException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = 'The character sheet you specified does not exist.'

    def __init__(self) -> None:
        super().__init__(self.status_code, detail=self.detail)

    def __str__(self) -> str:
        return self.detail
