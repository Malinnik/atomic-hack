from aiohttp import web

from endpoints.test import GetFile, GetFile2

def setup_routes(app: web.Application):
    """Инициализация роутов"""
    app.add_routes(
        [
            # Test of recieveng files
           web.view('/api/v1/test', GetFile),
           web.view('/api/v2/test', GetFile2),
        ]
    )
