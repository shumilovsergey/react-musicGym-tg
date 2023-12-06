from typing import Union
from pydantic import BaseModel
import asyncio
import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from const import TG_TOKEN
import requests
import json





app = FastAPI()

# app.mount("/build", StaticFiles(directory="build", html=True), name="build")


class Item(BaseModel):
    name: str
    price: int
    is_offer: Union[bool, None] = None


@app.get("/")
def read_root():
    return {"Hello": "This is py-musicGym-tg bot"}

@app.get("/app")
async def get_app():
    
    return RedirectResponse("http://10.12.0.93:3000")


@app.post("/bot")
async def print_request(request: Request):
    body = await request.json()
   
    text = "Чтобы зайти в магазин Шумилова - нажимайте кнопку 👇 "
    chat_id = body["message"]["chat"]["id"]
    

    web_app_info = {"url": "https://22e0-91-151-178-189.ngrok-free.app/app"}
    keyboard = {
        "inline_keyboard" :  [
            [
                {'text': 'Аудио', "web_app_info": web_app_info}
            ],
        ]
    }

    
    data = { 
        "chat_id": chat_id,
        "text": text,
        "reply_markup" : json.dumps(keyboard)
    }
    response = requests.post(f"https://api.telegram.org/bot{TG_TOKEN}/sendMessage", data)

    print(response)
    return 