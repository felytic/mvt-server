from aiohttp import web

from tile_manager import TileManager


async def get_tile(request):
    manager = TileManager(request.app)
    result = await manager.get_tile(**request.match_info)

    return web.Response(
        status=200,
        body=result,
        headers={
            'Content-Type': "application/x-protobuf",
        }
    )
