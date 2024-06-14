import os
import asyncio
from aiohttp import web
from sqlalchemy.ext.asyncio import create_async_engine
from core.orm import Base
from aiohttp_pydantic import oas

from core.routes import setup_routes


async def create_app():
    app = web.Application(client_max_size=4 * 1024 * 1024)
    # app["db_engine"] = create_async_engine(
    #     os.getenv("POSTGRES_URL"),
    #     pool_size=4,
    #     max_overflow=8,
    #     pool_recycle=120,
    #     pool_pre_ping=True,
    #     future=True,
    # )
    # app["tasks"] = {}
    setup_routes(app)

    # async with app["db_engine"].begin() as session:
    #     # FIX: coment line below before deploying server
    #     await session.run_sync(Base.metadata.drop_all)
    #     await session.run_sync(Base.metadata.create_all)

    oas.setup(app, title_spec="Service Name", version_spec="0.1.0")

    return app
