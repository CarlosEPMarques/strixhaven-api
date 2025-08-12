from starlette import status
from starlette.exceptions import HTTPException

class StoreItemInvalidStoreIdException(HTTPException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY

    def __init__(self, store_id: str):
        detail = f'Invalid Store ID: {store_id}'
        super().__init__(self.status_code, detail=detail)

class StoreItemInvalidNameException(HTTPException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY

    def __init__(self, name: str):
        detail = f'Invalid Store Item Name: {name}'
        super().__init__(self.status_code, detail=detail)

class StoreItemInvalidDescriptionException(HTTPException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY

    def __init__(self, description: str):
        detail = f'Invalid Store Item Description: {description}'
        super().__init__(self.status_code, detail=detail)

class StoreItemInvalidPriceException(HTTPException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY

    def __init__(self, price: str):
        detail = f'Invalid Store Item Price: {price}'
        super().__init__(self.status_code, detail=detail)

class StoreItemInvalidImageUrlException(HTTPException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY

    def __init__(self, image_url: str):
        detail = f'Invalid Store Item Image URL: {image_url}'
        super().__init__(self.status_code, detail=detail)

class StoreItemNotFoundException(HTTPException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = 'The store item you specified does not exist.'
    
    def __init__(self):
        super().__init__(self.status_code, detail=self.detail)

    def __str__(self) -> str:
        return self.detail

class StoreItemsNotFoundException(HTTPException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = 'No store items were found.'

    def __init__(self):
        super().__init__(self.status_code, detail=self.detail)

    def __str__(self) -> str:
        return self.detail
