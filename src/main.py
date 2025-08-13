from fastapi.routing import APIRouter

from src.modules.book import book_router
from src.modules.calendar_note import calendar_note_router
from src.modules.character_note import character_note_router
from src.modules.character_sheet import character_sheet_router
from src.modules.classes import class_router
from src.modules.college import college_router
from src.modules.event_note import event_note_router
from src.modules.inventory_item import inventory_item_router
from src.modules.map import map_router
from src.modules.monster import monster_router
from src.modules.news import news_router
from src.modules.note import note_router
from src.modules.npc import npc_router
from src.modules.npc_note import npc_note_router
from src.modules.npc_reputation import npc_reputation_router
from src.modules.player_character import player_character_router
from src.modules.store_item import store_item_router
from src.modules.store import store_router
from src.modules.user import user_router

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