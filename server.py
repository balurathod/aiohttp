from aiohttp import web

async def hello(request):
    return web.Response(text="Hello, aiohttp is working!")

app = web.Application()
app.router.add_get('/', hello)

if __name__ == '__main__':
    web.run_app(app, host='0.0.0.0', port=8080)
