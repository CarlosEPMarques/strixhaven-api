from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.modules.book.book_repository import BookRepository
from src.modules.book.book_usecase import BookUseCase
from src.settings.database.sqlalchemy.database import get_session


def book_usecase_factory(
    database: AsyncSession = Depends(get_session),
) -> BookUseCase:
    book_repository = BookRepository(database)
    return BookUseCase(book_repository)
