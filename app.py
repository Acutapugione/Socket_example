from quart import Quart
import asyncio


app = Quart(__name__)


@app.get("/")
async def index():
    await asyncio.sleep(1)
    return {
        "name": "Vasya",
        "age": 21,
    }
