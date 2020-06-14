class TileManager:
    def __init__(self, app):
        self.db = app['db']

    async def get_tile(self, schema: str, table: str, x: int, y: int, z: int,
                       column='geometry', extra_columns=None):

        cols = ', ' + ', '.join(extra_columns) if extra_columns else ''

        query = f"""
            WITH mvtgeom AS
            (
              SELECT
                  ST_AsMVTGeom(
                      ST_Transform(
                        {column},
                        3857
                      ),
                      ST_TileEnvelope({z}, {x}, {y})
                  ) AS geom
                  {cols}
              FROM {schema}.{table}
              WHERE ST_Intersects(
                  {column},
                  ST_Transform(
                    ST_TileEnvelope({z}, {x}, {y}),
                    4326
                  )
              )
            )
            SELECT ST_AsMVT(mvtgeom.*)
            FROM mvtgeom;
        """

        async with self.db.acquire() as conn:
            result = await conn.scalar(query)

        return bytes() if result is None else bytes(result)
