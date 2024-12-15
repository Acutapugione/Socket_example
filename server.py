from aiohttp import web
import socketio

sio = socketio.AsyncServer()
app = web.Application()
sio.attach(app)


async def index(request):
    """Serve the client-side application."""
    with open("index.html") as f:
        return web.Response(text=f.read(), content_type="text/html")


@sio.event
async def connect(sid, environ):
    # await sio.emit("my_message", data="hello")
    print("connect ", sid)


@sio.event
async def my_message(sid, data):
    print("message ", data)


@sio.event
def disconnect(sid):
    print("disconnect ", sid)


app.router.add_static("/static", "static")
app.router.add_get("/", index)

if __name__ == "__main__":
    web.run_app(app, host="localhost", port=5000)
