from src.modules.book.entity import Book
from src.modules.book.repository import BookRepository
from src.modules.book.value_object import BookTitle


async def test_crud_book(book_repository: BookRepository, book: Book) -> None:
    # Create
    await book_repository.find_by_section(book.section)
    await book_repository.create(book)
    created_book = await book_repository.find(book.id)
    assert created_book is not None

    # Read
    found_book = await book_repository.find(book.id)
    assert found_book is not None
    assert found_book.title == book.title

    # Update
    new_title = 'The Hobbit'
    found_book.update_title(BookTitle(new_title))
    await book_repository.update(found_book)
    updated_book = await book_repository.find(found_book.id)
    assert updated_book is not None
    assert updated_book.title == found_book.title

    # Delete
    await book_repository.delete(updated_book)
    deleted_book = await book_repository.find(updated_book.id)
    assert deleted_book is None
