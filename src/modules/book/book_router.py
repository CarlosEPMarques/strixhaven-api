from typing import Annotated

from fastapi.param_functions import Depends
from fastapi.routing import APIRouter
from starlette import status

from src.modules.book.book_injection import book_usecase_factory
from src.modules.book.book_schema import BookCreateInput, BookOutput, BookUpdateInput
from src.modules.book.book_usecase import BookUseCase

router = APIRouter(prefix='/books', tags=['Books'])


@router.post('', status_code=status.HTTP_201_CREATED)
async def create_book(
    input_data: BookCreateInput, usecase: Annotated[BookUseCase, Depends(book_usecase_factory)]
) -> BookOutput:
    return await usecase.create_book(input_data=input_data)


@router.get('', status_code=status.HTTP_200_OK)
async def get_books(
    usecase: Annotated[BookUseCase, Depends(book_usecase_factory)],
) -> list[BookOutput]:
    return await usecase.find_books()


@router.get('/{book_id}', status_code=status.HTTP_200_OK)
async def get_book(
    book_id: str, usecase: Annotated[BookUseCase, Depends(book_usecase_factory)]
) -> BookOutput:
    return await usecase.find_book(book_id=book_id)


@router.put('/{book_id}', status_code=status.HTTP_202_ACCEPTED)
async def update_book(
    book_id: str,
    input_data: BookUpdateInput,
    usecase: Annotated[BookUseCase, Depends(book_usecase_factory)],
) -> BookOutput:
    return await usecase.update_book(book_id=book_id, input_data=input_data)


@router.delete('/{book_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(
    book_id: str, usecase: Annotated[BookUseCase, Depends(book_usecase_factory)]
) -> None:
    return await usecase.delete_book(book_id=book_id)
