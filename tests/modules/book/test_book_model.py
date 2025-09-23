from src.modules.book.entity import Book
from src.modules.book.model import BookModel


def test_book_model_from_entity(book: Book) -> None:
    book_model = BookModel.from_entity(book)

    assert book_model.external_id == book.id
    assert book_model.title == book.title
    assert book_model.summary == book.summary
    assert book_model.section == book.section
    assert book_model.is_hidden == book.is_hidden
    assert book_model.image_url == book.image_url


def test_book_model_to_entity(book: Book) -> None:
    book_model = BookModel.from_entity(book)
    entity = book_model.to_entity()

    assert entity.id == book.id
    assert entity.title == book.title
    assert entity.summary == book.summary
    assert entity.section == book.section
    assert entity.is_hidden == book.is_hidden
    assert entity.image_url == book.image_url
