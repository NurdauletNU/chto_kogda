from sanic import Sanic
from sanic.response import json

app = Sanic("MyApp")


@app.get("/api")
async def api(request):
    data = {"name": "Nurdaulet", "items": [i for i in range(1, 11)]}
    return json({"data": data})