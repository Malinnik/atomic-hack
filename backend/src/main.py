import logging
import os
from aiohttp import web
from dotenv import load_dotenv

from core.app import create_app

load_dotenv()


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, filename='backend.log', filemode='w')
    logging.info("Starting server...")
    app = create_app()

    web.run_app(app, host='0.0.0.0', port=int(os.getenv('APP_PORT', 8080)))
