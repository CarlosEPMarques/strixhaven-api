from httpx import AsyncClient
from starlette import status

from src.modules.book.book_entity import Book
from src.modules.book.book_repository import BookRepository


async def test_crud_book(client: AsyncClient, book: Book) -> None:
    # Create
    response = await client.post(
        '/books',
        json={
            'title': book.title,
            'summary': book.summary,
            'section': book.section,
            'is_hidden': book.is_hidden,
            'image_url': book.image_url,
        },
    )
    output = response.json()
    assert response.status_code == status.HTTP_201_CREATED
    assert output['id'] is not None
    assert output['title'] == book.title
    assert output['summary'] == book.summary
    assert output['section'] == book.section
    assert output['is_hidden'] == book.is_hidden
    assert output['image_url'] == book.image_url

    # Read
    response = await client.get(f'/books/{output["id"]}')
    output = response.json()
    assert response.status_code == status.HTTP_200_OK
    assert output['title'] == book.title
    assert output['summary'] == book.summary
    assert output['section'] == book.section
    assert output['is_hidden'] == book.is_hidden
    assert output['image_url'] == book.image_url

    # Update
    updated_summary = 'Run you fools!'
    response = await client.put(f'/books/{output["id"]}', json={'summary': updated_summary})
    output = response.json()

    assert response.status_code == status.HTTP_202_ACCEPTED
    assert output['title'] == book.title
    assert output['summary'] == updated_summary
    assert output['section'] == book.section
    assert output['is_hidden'] == book.is_hidden
    assert output['image_url'] == book.image_url

    # Delete
    response = await client.delete(f'/books/{output["id"]}')
    assert response.status_code == status.HTTP_204_NO_CONTENT


async def test_get_books(
    client: AsyncClient,
    book: Book,
    book_2: Book,
    book_repository: BookRepository,
) -> None:
    await book_repository.create(book=book)
    await book_repository.create(book=book_2)
    response = await client.get('/books')
    output = response.json()
    assert response.status_code == status.HTTP_200_OK
    output_ids = [book['id'] for book in output]
    assert str(book.id) in output_ids
    assert str(book_2.id) in output_ids
    await book_repository.delete(book=book)
    await book_repository.delete(book=book_2)
