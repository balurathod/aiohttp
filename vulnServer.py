from aiohttp import web

app = web.Application()
# Vulnerable static route (follow_symlinks=True)
app.router.add_static('/static/', path='static', follow_symlinks=True)

async def hello(request):
    return web.Response(text="Hello, From Vulnerable aiohttp!  ")

app.router.add_get('/', hello)

if __name__ == '__main__':
    web.run_app(app, port=8080)