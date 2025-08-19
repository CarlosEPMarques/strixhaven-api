from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import delete, select

from src.modules.book.book_entity import Book
from src.modules.book.book_model import BookModel


class BookRepository:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def create(self, book: Book) -> None:
        book_model = BookModel.from_entity(book)
        self.session.add(book_model)
        await self.session.commit()

    async def update(self, book: Book) -> None:
        query = select(BookModel).where(BookModel.id == book.id)
        result = await self.session.execute(query)
        book_model = result.scalars().one()
        book_model.title = book.title
        book_model.summary = book.summary
        book_model.section = book.section
        book_model.is_hidden = book.is_hidden
        book_model.image_url = book.image_url
        await self.session.commit()

    async def delete(self, book: Book) -> None:
        query = delete(BookModel).where(BookModel.id == book.id)
        await self.session.execute(query)
        await self.session.commit()

    async def find(self, book_id: str) -> Book | None:
        if book_id:
            query = select(BookModel).where(BookModel.id == book_id)

        try:
            result = await self.session.execute(query)
            book_model = result.scalars().one()
            return book_model.to_entity()
        except NoResultFound:
            return None

    async def find_by_section(self, book_section: str) -> list[Book] | None:
        if book_section:
            query = select(BookModel).where(BookModel.section == book_section)

        try:
            result = await self.session.execute(query)
            book_models = result.scalars().all()
            return [book_model.to_entity() for book_model in book_models]
        except NoResultFound:
            return None

    async def find_all(self) -> list[Book] | None:
        query = select(BookModel)
        result = await self.session.execute(query)
        book_models = result.scalars().all()
        return [book_model.to_entity() for book_model in book_models]
