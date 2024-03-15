import datetime

import pytest
import pytz
from httpx import AsyncClient

from app.core import settings
from app.start_line_provider import app

base_url = "http://localhost"


class TestEvent:
    @pytest.mark.asyncio
    async def test_create_get_event(self) -> None:
        async with AsyncClient(app=app, base_url=base_url) as client:
            data = {"coefficient": 1.22,
                    "deadline_ts": (datetime.datetime.now(tz=pytz.UTC)).timestamp()}
            r = await client.put(
                f"{settings.API_V1_STR}/event",
                json=data
            )
            print(r.content)
            assert r.status_code == 200
            r = await client.get(
                f"{settings.API_V1_STR}/event/{r.json()['id']}"
            )
            assert r.status_code == 200

    @pytest.mark.asyncio
    async def test_get_all_events(self) -> None:
        async with AsyncClient(app=app, base_url=base_url) as client:
            r = await client.get(
                f"{settings.API_V1_STR}/events"
            )
        assert r.status_code == 200
