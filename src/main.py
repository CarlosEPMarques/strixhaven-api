from fastapi.routing import APIRouter

from src.routers import (
    book_router,
    calendar_note_router,
    character_note_router,
    character_sheet_router,
    class_router,
    college_router,
    event_note_router,
    inventory_item_router,
    map_router,
    monster_router,
    news_router,
    note_router,
    npc_router,
    npc_note_router,
    npc_reputation_router,
    player_character_router,
    session_router,
    store_item_router,
    store_router,
    user_router
)
from src.settings.server.fastapi import app

routers: list[APIRouter] = [
    book_router,
    calendar_note_router,
    character_note_router,
    character_sheet_router,
    class_router,
    college_router,
    event_note_router,
    inventory_item_router,
    map_router,
    monster_router,
    news_router,
    note_router,
    npc_router,
    npc_note_router,
    npc_reputation_router,
    player_character_router,
    session_router,
    store_item_router,
    store_router,
    user_router
]
routers.sort(key=lambda router: router.prefix)

def sort_routes_by_path(router: APIRouter) -> None:
    router.routes.sort(key=lambda route: route.path) # type: ignore[attr-defined]
    
for router in routers:
    sort_routes_by_path(router)
    app.include_router(router)