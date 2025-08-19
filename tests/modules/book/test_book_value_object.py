import pytest
from src.modules.book.book_value_object import (
    BookID,
    BookTitle,
    BookSummary,
    BookSection,
    BookIsHidden,
    BookImageUrl,
)
from src.modules.book.book_exception import (
    BookInvalidImageUrlException,
    BookInvalidIsHiddenException,
    BookInvalidSectionException,
    BookInvalidSummaryException,
    BookInvalidTitleException,
)


# ID
def test_constructor_should_create_instance() -> None:
    value = "123e4567-e89b-12d3-a456-426614174000"
    book_id = BookID(value)
    assert book_id.value == value


def test_generate_should_create_instance() -> None:
    book_id = BookID.generate()
    assert isinstance(book_id, BookID)
    assert book_id.value is not None


def test_str_should_return_string_representation() -> None:
    value = "123e4567-e89b-12d3-a456-426614174000"
    book_id = BookID(value)
    assert str(book_id) == value


# Title
@pytest.mark.parametrize(
    "title",
    ["The Silmarillion", "The Adventures of Tom Bombadil", "The Fall of Gondolin"],
)
def test_constructor_should_create_instance(title: str) -> None:
    book_title = BookTitle(title)
    assert book_title.value == title


@pytest.mark.parametrize("title", ["", "A", "Invalid@Title", "X" * 101])
def test_constructor_should_raise_exception(title: str) -> None:
    with pytest.raises(BookInvalidTitleException):
        BookTitle(title)


# Summary
@pytest.mark.parametrize("summary", ["This is a valid summary." * 1, "A" * 5000])
def test_constructor_should_create_instance(summary: str) -> None:
    book_summary = BookSummary(summary)
    assert book_summary.value == summary


@pytest.mark.parametrize("summary", ["", "Too short", "A" * 5001])
def test_constructor_should_raise_exception(summary: str) -> None:
    with pytest.raises(BookInvalidSummaryException):
        BookSummary(summary)


# Section
@pytest.mark.parametrize("section", ["Fiction", "Science 101", "Section-1"])
def test_constructor_should_create_instance(section: str) -> None:
    book_section = BookSection(section)
    assert book_section.value == section


@pytest.mark.parametrize("section", ["", "A", "Invalid#Section", "X" * 101])
def test_constructor_should_raise_exception(section: str) -> None:
    with pytest.raises(BookInvalidSectionException):
        BookSection(section)


# Is Hidden
@pytest.mark.parametrize("hidden", [True, False])
def test_constructor_should_create_instance(hidden: bool) -> None:
    book_hidden = BookIsHidden(hidden)
    assert book_hidden.value is hidden


@pytest.mark.parametrize("hidden", ["true", 1, None])
def test_constructor_should_raise_exception(hidden) -> None:
    with pytest.raises(BookInvalidIsHiddenException):
        BookIsHidden(hidden)


# Image URL
@pytest.mark.parametrize(
    "url", ["http://example.com/image.png", "https://example.com/img.jpg"]
)
def test_constructor_should_create_instance(url: str) -> None:
    book_image = BookImageUrl(url)
    assert book_image.value == url


@pytest.mark.parametrize(
    "url", ["ftp://example.com/image.png", "example.com/img.jpg", "", None]
)
def test_constructor_should_raise_exception(url) -> None:
    with pytest.raises(BookInvalidImageUrlException):
        BookImageUrl(url)
