from views import get_tile


def setup_routes(app):
    app.router.add_get(
        app['settings'].ROUTE_PREFIX +
        '{schema:[A-z,0-9]+}.{table:[A-z,0-9]+}'
        '/{z:[0-9]+}/{x:[0-9]+}/{y:[0-9]+}',
        get_tile
    )
