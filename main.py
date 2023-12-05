from typing import Union
from pydantic import BaseModel
import asyncio
import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# app.mount("/build", StaticFiles(directory="build", html=True), name="build")


class Item(BaseModel):
    name: str
    price: int
    is_offer: Union[bool, None] = None


@app.get("/")
def read_root():
    return {"Hello": "This is py-musicGym-tg bot"}

@app.get("/build")
async def get_app():
    return FileResponse("build/index.html")



@app.post("/bot")
async def print_request(request: Request):
    body = await request.json()
    print(body)
    
    return 