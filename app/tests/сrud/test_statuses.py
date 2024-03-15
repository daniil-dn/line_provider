import pytest

from app.crud import crud_event_status
from app.db.session import SessionLocal

@pytest.mark.asyncio
async def test_event_statuses(session: SessionLocal) -> None:
    async with session:
        event_statuses = await crud_event_status.get_all(session)
    assert len(event_statuses) >= 3
    for status in event_statuses:
        if status.id == 1:
            assert status.name_id == 'not_finished'
        elif status.id == 2:
            assert status.name_id == 'first_win'
        elif status.id == 3:
            assert status.name_id == 'second_win'
