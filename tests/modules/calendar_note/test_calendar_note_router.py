from httpx import AsyncClient
from starlette import status

from src.modules.calendar_note.calendar_note_entity import CalendarNote


async def test_crud_calendar_note(client: AsyncClient, calendar_note: CalendarNote) -> None:
    game_datetime = calendar_note.game_datetime.strftime('%Y-%m-%dT%H:%M:%S')
    # Create
    response = await client.post(
        '/calendar-notes',
        json={
            'title': calendar_note.title,
            'description': calendar_note.description,
            'game_datetime': str(calendar_note.game_datetime),
            'is_exam': calendar_note.is_exam,
        },
    )
    output = response.json()
    assert response.status_code == status.HTTP_201_CREATED
    assert output['id'] is not None
    assert output['title'] == calendar_note.title
    assert output['description'] == calendar_note.description
    assert output['game_datetime'] == game_datetime
    assert output['is_exam'] == calendar_note.is_exam

    # Read
    response = await client.get(f'/calendar-notes/{output["id"]}')
    output = response.json()
    assert response.status_code == status.HTTP_200_OK
    assert output['title'] == calendar_note.title
    assert output['description'] == calendar_note.description
    assert output['game_datetime'] == game_datetime
    assert output['is_exam'] == calendar_note.is_exam

    # Update
    updated_description = 'Pay attention to the class!'
    response = await client.put(
        f'/calendar-notes/{output["id"]}', json={'description': updated_description}
    )
    output = response.json()

    assert response.status_code == status.HTTP_202_ACCEPTED
    assert output['title'] == calendar_note.title
    assert output['description'] == updated_description
    assert output['game_datetime'] == game_datetime
    assert output['is_exam'] == calendar_note.is_exam

    # Delete
    response = await client.delete(f'/calendar-notes/{output["id"]}')
    assert response.status_code == status.HTTP_204_NO_CONTENT


async def test_get_calendar_notes_by_game_month(
    client: AsyncClient, calendar_note: CalendarNote, calendar_note_2: CalendarNote
) -> None:
    response_1 = await client.post(
        '/calendar-notes',
        json={
            'title': calendar_note.title,
            'description': calendar_note.description,
            'game_datetime': str(calendar_note.game_datetime),
            'is_exam': calendar_note.is_exam,
        },
    )
    calendar_note_id = response_1.json()['id']
    response_2 = await client.post(
        '/calendar-notes',
        json={
            'title': calendar_note_2.title,
            'description': calendar_note_2.description,
            'game_datetime': str(calendar_note_2.game_datetime),
            'is_exam': calendar_note_2.is_exam,
        },
    )
    calendar_note_2_id = response_2.json()['id']

    game_month = calendar_note.game_datetime.month
    response = await client.get(f'/calendar-notes/month/{game_month}')
    assert response.status_code == 200
    output = response.json()
    assert all(f'-{game_month:02}-' in item['game_datetime'] for item in output)
    await client.delete(f'/calendar-notes/{calendar_note_id}')
    await client.delete(f'/calendar-notes/{calendar_note_2_id}')


async def test_get_calendar_notes(
    client: AsyncClient, calendar_note: CalendarNote, calendar_note_2: CalendarNote
) -> None:
    response_1 = await client.post(
        '/calendar-notes',
        json={
            'title': calendar_note.title,
            'description': calendar_note.description,
            'game_datetime': str(calendar_note.game_datetime),
            'is_exam': calendar_note.is_exam,
        },
    )
    calendar_note_id = response_1.json()['id']
    response_2 = await client.post(
        '/calendar-notes',
        json={
            'title': calendar_note_2.title,
            'description': calendar_note_2.description,
            'game_datetime': str(calendar_note_2.game_datetime),
            'is_exam': calendar_note_2.is_exam,
        },
    )
    calendar_note_2_id = response_2.json()['id']
    response = await client.get('/calendar-notes')
    output = response.json()
    assert response.status_code == status.HTTP_200_OK
    output_ids = [calendar_note['id'] for calendar_note in output]
    assert str(calendar_note_id) in output_ids
    assert str(calendar_note_2_id) in output_ids
    await client.delete(f'/calendar-notes/{calendar_note_id}')
    await client.delete(f'/calendar-notes/{calendar_note_2_id}')
