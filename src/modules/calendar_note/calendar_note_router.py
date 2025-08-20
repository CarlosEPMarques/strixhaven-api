from typing import Annotated

from fastapi.param_functions import Depends
from fastapi.routing import APIRouter
from starlette import status

from src.modules.calendar_note.calendar_note_injection import calendar_note_usecase_factory
from src.modules.calendar_note.calendar_note_schema import (
    CalendarNoteCreateInput,
    CalendarNoteOutput,
    CalendarNoteUpdateInput,
)
from src.modules.calendar_note.calendar_note_usecase import CalendarNoteUseCase

router = APIRouter(prefix='/calendar-notes', tags=['Calendar-Notes'])


@router.post('', status_code=status.HTTP_201_CREATED)
async def create_calendar_note(
    input_data: CalendarNoteCreateInput,
    usecase: Annotated[CalendarNoteUseCase, Depends(calendar_note_usecase_factory)],
) -> CalendarNoteOutput:
    return await usecase.create_calendar_note(input_data=input_data)


@router.get('', status_code=status.HTTP_200_OK)
async def get_calendar_notes(
    usecase: Annotated[CalendarNoteUseCase, Depends(calendar_note_usecase_factory)],
) -> list[CalendarNoteOutput]:
    return await usecase.find_calendar_notes()


@router.get('/{calendar_note_id}', status_code=status.HTTP_200_OK)
async def get_calendar_note(
    calendar_note_id: str,
    usecase: Annotated[CalendarNoteUseCase, Depends(calendar_note_usecase_factory)],
) -> CalendarNoteOutput:
    return await usecase.find_calendar_note_by_id(calendar_note_id=calendar_note_id)


@router.get('/month/{calendar_month}', status_code=status.HTTP_200_OK)
async def get_calendar_notes_by_game_month(
    calendar_month: int,
    usecase: Annotated[CalendarNoteUseCase, Depends(calendar_note_usecase_factory)],
) -> list[CalendarNoteOutput]:
    return await usecase.find_calendar_note_by_month(calendar_month=calendar_month)


@router.put('/{calendar_note_id}', status_code=status.HTTP_202_ACCEPTED)
async def update_calendar_note(
    calendar_note_id: str,
    input_data: CalendarNoteUpdateInput,
    usecase: Annotated[CalendarNoteUseCase, Depends(calendar_note_usecase_factory)],
) -> CalendarNoteOutput:
    return await usecase.update_calendar_note(
        calendar_note_id=calendar_note_id, input_data=input_data
    )


@router.delete('/{calendar_note_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_calendar_note(
    calendar_note_id: str,
    usecase: Annotated[CalendarNoteUseCase, Depends(calendar_note_usecase_factory)],
) -> None:
    return await usecase.delete_calendar_note(calendar_note_id=calendar_note_id)
