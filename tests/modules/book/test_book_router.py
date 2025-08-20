from httpx import AsyncClient
from starlette import status

from src.modules.book.book_entity import Book


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
) -> None:
    response_1 = await client.post(
        '/books',
        json={
            'title': book.title,
            'summary': book.summary,
            'section': book.section,
            'is_hidden': book.is_hidden,
            'image_url': book.image_url,
        },
    )
    book_id = response_1.json()['id']
    response_2 = await client.post(
        '/books',
        json={
            'title': book_2.title,
            'summary': book_2.summary,
            'section': book_2.section,
            'is_hidden': book_2.is_hidden,
            'image_url': book_2.image_url,
        },
    )
    book_2_id = response_2.json()['id']
    response = await client.get('/books')
    output = response.json()
    assert response.status_code == status.HTTP_200_OK
    output_ids = [book['id'] for book in output]
    assert str(book_id) in output_ids
    assert str(book_2_id) in output_ids
    await client.delete(f'/calendar-notes/{book_id}')
    await client.delete(f'/calendar-notes/{book_2_id}')
