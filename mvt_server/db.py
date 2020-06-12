import aiopg.sa


async def init_pg(app):
    settings = app['settings']

    engine = await aiopg.sa.create_engine(
        database=settings.DB_NAME,
        user=settings.DB_USER,
        password=settings.DB_PASS,
        host=settings.DB_HOST,
        port=settings.DB_PORT
    )

    app['db'] = engine


async def close_pg(app):
    app['db'].close()
    await app['db'].wait_closed()

