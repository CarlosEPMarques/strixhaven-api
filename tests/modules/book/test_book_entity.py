from src.modules.book.book_entity import Book
from src.modules.book.book_value_object import (
    BookImageUrl,
    BookIsHidden,
    BookSection,
    BookSummary,
    BookTitle,
)


def test_constructor_should_create_instance(book: Book) -> None:
    assert book.id is not None
    assert book.title == 'The Lord of the Rings - The Two Towers'
    assert book.summary == 'My precious'
    assert book.section == 'Fantasy'
    assert book.is_hidden is False
    assert book.image_url == 'http://lotr-images.com/gollum'


def test_update_book_title(book: Book) -> None:
    book.update_title(BookTitle('The Lord of the Rings - The Return of the King'))
    assert book.title == 'The Lord of the Rings - The Return of the King'


def test_update_book_summary(book: Book) -> None:
    book.update_summary(BookSummary('One ring to rule them all.'))
    assert book.summary == 'One ring to rule them all.'


def test_update_book_section(book: Book) -> None:
    book.update_section(BookSection('Science Fiction'))
    assert book.section == 'Science Fiction'


def test_update_book_is_hidden(book: Book) -> None:
    book.update_is_hidden(BookIsHidden(value=True))
    assert book.is_hidden is True


def test_update_book_image_url(book: Book) -> None:
    book.update_image_url(BookImageUrl('http://lotr-images.com/gandalf'))
    assert book.image_url == 'http://lotr-images.com/gandalf'
