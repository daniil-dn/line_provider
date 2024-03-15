import asyncio

from app.crud import crud_event_status
from app.db import SessionLocal
from app.logs import server_log
from app.models import EventStatus
from app.schemas import crud_schemas

__doc__ = """Заполняет базу данных при старте приложения"""


async def fill_db():
    async with SessionLocal() as db:
        server_log.info('FILL DB')
        events_statuses: list[EventStatus] = await crud_event_status.get_all(db)
        if not events_statuses:
            await crud_event_status.create(
                db, obj_in=crud_schemas.EventStatusCreate(
                    id=1, name_id='not_finished', name='Незавершённое'
                )
            )
            await crud_event_status.create(
                db, obj_in=crud_schemas.EventStatusCreate(
                    id=2, name_id='first_win', name='Завершено выигрышем первой команды'
                )
            )
            await crud_event_status.create(
                db, obj_in=crud_schemas.EventStatusCreate(
                    id=3, name_id='second_win', name='Завершено выигрышем второй команды'
                )
            )


if __name__ == "__main__":
    asyncio.run(fill_db())
