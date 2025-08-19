import pytest
from src.modules.book.book_entity import Book
from src.modules.book.book_repository import BookRepository
from src.modules.book.book_usecase import BookUseCase
from src.modules.book.book_value_object import (
    BookTitle,
    BookSummary,
    BookSection,
    BookIsHidden,
    BookImageUrl,
)

@pytest.fixture
def book() -> Book:
    book_title = BookTitle("The Lord of the Rings - The Two Towers")
    book_summary = BookSummary("My precious")
    book_section = BookSection("Fantasy")
    book_is_hidden = BookIsHidden(False)
    book_image_url = BookImageUrl("http://lotr-images.com/gollum")
    return Book.create(
        title=book_title,
        summary=book_summary,
        section=book_section,
        is_hidden=book_is_hidden,
        image_url=book_image_url,
    )
    
@pytest.fixture
async def book_2() -> Book:
    book_title = BookTitle("The Lord of the Rings - The Return of the King")
    book_summary = BookSummary("For Frodo!")
    book_section = BookSection("Fantasy")
    book_is_hidden = BookIsHidden(False)
    book_image_url = BookImageUrl("http://lotr-images.com/gollum")
    return Book.create(
        title=book_title,
        summary=book_summary,
        section=book_section,
        is_hidden=book_is_hidden,
        image_url=book_image_url,
    )

@pytest.fixture
def book_repository() -> BookRepository:
    return BookRepository
    
@pytest.fixture
def book_usecase(book_repository: BookRepository) -> BookUseCase:
    return BookUseCase(book_repository)