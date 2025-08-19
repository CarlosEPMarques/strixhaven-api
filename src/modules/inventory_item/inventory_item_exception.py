from typing import Any

from starlette import status
from starlette.exceptions import HTTPException


class InventoryItemInvalidCharacterIdException(HTTPException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY

    def __init__(self, character_id: str) -> None:
        detail = f'Invalid Character ID: {character_id}'
        super().__init__(self.status_code, detail=detail)


class InventoryItemInvalidItemIdException(HTTPException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY

    def __init__(self, item_id: str) -> None:
        detail = f'Invalid Item ID: {item_id}'
        super().__init__(self.status_code, detail=detail)


class InventoryItemInvalidAmountException(HTTPException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY

    def __init__(self, amount: int) -> None:
        detail = f'Invalid Amount: {amount}'
        super().__init__(self.status_code, detail=detail)


class InventoryItemInvalidMetadataException(HTTPException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY

    def __init__(self, metadata: dict[str, Any]) -> None:
        detail = f'Invalid Metadata: {metadata}'
        super().__init__(self.status_code, detail=detail)


class InventoryItemsNotFoundException(HTTPException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = 'No inventory items were found.'

    def __init__(self) -> None:
        super().__init__(status_code=self.status_code, detail=self.detail)

    def __str__(self) -> str:
        return self.detail
