from aiohttp import web

from endpoints.detection import Detection

def setup_routes(app: web.Application):
    """Инициализация роутов"""
    app.add_routes(
        [
           web.view('/api/v2/test', Detection),
        ]
    )
