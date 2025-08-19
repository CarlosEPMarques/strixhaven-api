from typing import cast

from src.modules.book.book_entity import Book
from src.modules.book.book_exception import BookNotFoundException, BooksNotFoundException
from src.modules.book.book_repository import BookRepository
from src.modules.book.book_schema import BookCreateInput, BookOutput, BookUpdateInput
from src.modules.book.book_value_object import (
    BookImageUrl,
    BookIsHidden,
    BookSection,
    BookSummary,
    BookTitle,
)


class BookUseCase:
    def __init__(self, book_repository: BookRepository) -> None:
        self.book_repository = book_repository

    async def create_book(self, input_data: BookCreateInput) -> BookOutput:
        book = input_data.to_entity()
        await self.book_repository.create(book)
        created_book = await self.book_repository.find(book_id=book.id)
        return BookOutput.from_entity(cast(Book, created_book))

    async def update_book(self, book_id: str, input_data: BookUpdateInput) -> BookOutput:
        book = await self.book_repository.find(book_id=book_id)
        if not book:
            raise BookNotFoundException
        if input_data.title:
            book.update_title(BookTitle(input_data.title))
        if input_data.summary:
            book.update_summary(BookSummary(input_data.summary))
        if input_data.section:
            book.update_section(BookSection(input_data.section))
        if input_data.is_hidden:
            book.update_is_hidden(BookIsHidden(input_data.is_hidden))
        if input_data.image_url:
            book.update_image_url(BookImageUrl(input_data.image_url))
        await self.book_repository.update(book)
        updated_book = await self.book_repository.find(book_id=book.id)
        return BookOutput.from_entity(cast(Book, updated_book))

    async def delete_book(self, book_id: str) -> None:
        book = await self.book_repository.find(book_id=book_id)
        if not book:
            raise BookNotFoundException
        await self.book_repository.delete(book)

    async def find_book(self, book_id: str) -> BookOutput:
        book = await self.book_repository.find(book_id=book_id)
        if not book:
            raise BookNotFoundException
        return BookOutput.from_entity(book)

    async def find_books(self) -> list[BookOutput]:
        books = await self.book_repository.find_all()
        if not books:
            raise BooksNotFoundException
        return [BookOutput.from_entity(book) for book in books]
