from unittest.mock import AsyncMock

import pytest

from src.modules.book.entity import Book
from src.modules.book.exception import BookNotFoundException, BooksNotFoundException
from src.modules.book.repository import BookRepository
from src.modules.book.schema import BookCreateInput, BookOutput, BookUpdateInput
from src.modules.book.usecase import BookUseCase


async def test_create_book_usecase(
    book: Book, book_usecase: BookUseCase, book_repository: BookRepository
) -> None:
    book_repository.find_by_section = AsyncMock(return_value=None)
    book_repository.find = AsyncMock(return_value=book)
    book_repository.create = AsyncMock()
    input_data = BookCreateInput(
        title=book.title,
        summary=book.summary,
        section=book.section,
        is_hidden=book.is_hidden,
        image_url=book.image_url,
    )
    created_book = await book_usecase.create_book(input_data)

    assert created_book.id == book.id


async def test_update_book_title_usecase(
    book: Book, book_usecase: BookUseCase, book_repository: BookRepository
) -> None:
    book_repository.find = AsyncMock(return_value=book)
    book_repository.update = AsyncMock()
    updated_book_title = 'Hobbit'
    updated_book = await book_usecase.update_book(
        book_id=book.id, input_data=BookUpdateInput(title=updated_book_title)
    )

    assert updated_book.title == updated_book_title


async def test_update_book_summary_usecase(
    book: Book, book_usecase: BookUseCase, book_repository: BookRepository
) -> None:
    book_repository.find = AsyncMock(return_value=book)
    book_repository.update = AsyncMock()
    updated_book_summary = 'And this is Thorin Oakenshield, King under the Mountain.'
    updated_book = await book_usecase.update_book(
        book_id=book.id, input_data=BookUpdateInput(summary=updated_book_summary)
    )

    assert updated_book.summary == updated_book_summary


async def test_update_book_section_usecase(
    book: Book, book_usecase: BookUseCase, book_repository: BookRepository
) -> None:
    book_repository.find = AsyncMock(return_value=book)
    book_repository.update = AsyncMock()
    updated_book_section = 'Adventure'
    updated_book = await book_usecase.update_book(
        book_id=book.id, input_data=BookUpdateInput(section=updated_book_section)
    )

    assert updated_book.section == updated_book_section


async def test_update_book_is_hidden_usecase(
    book: Book, book_usecase: BookUseCase, book_repository: BookRepository
) -> None:
    book_repository.find = AsyncMock(return_value=book)
    book_repository.update = AsyncMock()
    updated_book_is_hidden = True
    updated_book = await book_usecase.update_book(
        book_id=book.id, input_data=BookUpdateInput(is_hidden=updated_book_is_hidden)
    )

    assert updated_book.is_hidden == updated_book_is_hidden


async def test_update_book_image_url_usecase(
    book: Book, book_usecase: BookUseCase, book_repository: BookRepository
) -> None:
    book_repository.find = AsyncMock(return_value=book)
    book_repository.update = AsyncMock()
    updated_book_image_url = 'http://lotr-images.com/bilbo_baggings'
    updated_book = await book_usecase.update_book(
        book_id=book.id, input_data=BookUpdateInput(image_url=updated_book_image_url)
    )

    assert updated_book.image_url == updated_book_image_url


async def test_update_book_not_found_usecase(
    book_usecase: BookUseCase,
    book_repository: BookRepository,
) -> None:
    book_repository.find = AsyncMock(return_value=None)

    with pytest.raises(BookNotFoundException) as error:
        await book_usecase.update_book(book_id='random-id', input_data=BookUpdateInput())

    assert str(error.value) == BookNotFoundException.detail


async def test_delete_book_usecase(
    book: Book,
    book_usecase: BookUseCase,
    book_repository: BookRepository,
) -> None:
    book_repository.find = AsyncMock(return_value=book)
    book_repository.delete = AsyncMock()
    await book_usecase.delete_book(book.id)

    book_repository.delete.assert_awaited_once_with(book)


async def test_delete_book_usecase_not_found(
    book_usecase: BookUseCase,
    book_repository: BookRepository,
) -> None:
    book_repository.find = AsyncMock(return_value=None)

    with pytest.raises(BookNotFoundException) as error:
        await book_usecase.delete_book('random-id')

    assert str(error.value) == BookNotFoundException.detail


async def test_find_book_usecase(
    book: Book,
    book_usecase: BookUseCase,
    book_repository: BookRepository,
) -> None:
    book_repository.find = AsyncMock(return_value=book)
    result = await book_usecase.find_book(book.id)

    assert result == BookOutput.from_entity(book)


async def test_find_book_usecase_not_found(
    book_usecase: BookUseCase, book_repository: BookRepository
) -> None:
    book_repository.find = AsyncMock(return_value=None)

    with pytest.raises(BookNotFoundException) as error:
        await book_usecase.find_book('non-existent-id')

    assert str(error.value) == BookNotFoundException.detail


async def test_find_books_usecase(
    book: Book,
    book_usecase: BookUseCase,
    book_repository: BookRepository,
) -> None:
    book_repository.find_all = AsyncMock(return_value=[book])
    result = await book_usecase.find_books()

    assert len(result) == 1


async def test_find_books_usecase_not_found(
    book_usecase: BookUseCase, book_repository: BookRepository
) -> None:
    book_repository.find_all = AsyncMock(return_value=None)

    with pytest.raises(BooksNotFoundException) as error:
        await book_usecase.find_books()

    assert str(error.value) == BooksNotFoundException.detail
