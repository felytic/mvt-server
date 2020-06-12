from aiohttp import web

from settings import Settings
from routes import setup_routes
from db import close_pg, init_pg

app = web.Application()
app['settings'] = Settings
setup_routes(app)
app.on_startup.append(init_pg)
app.on_cleanup.append(close_pg)
web.run_app(app)
