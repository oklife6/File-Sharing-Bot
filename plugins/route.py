#(©)Codexbotz
#rymme





from aiohttp import web

routes = web.RouteTableDef()

@routes.get("/", allow_head=True)
async def root_route_handler(request):
    web.Response(text="Engine Vroom Vroom")
