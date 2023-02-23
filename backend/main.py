
import os
from utils.settings import get_settings

if not os.path.exists(get_settings().static_path):
    os.makedirs(get_settings().static_path)

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware
from controller.api.chatGPT import router as chatGPT_route
import uvicorn


def create_app() -> FastAPI:
    app = FastAPI()
    app.mount('/static', StaticFiles(directory='./static'), name='static')
    app.debug = True

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(
        chatGPT_route,
        prefix='/api/v1/chatGPT',
        tags=['chatGPT'],
    )
    return app


app = create_app()


def start():
    global app
    uvicorn.run("main:app", **get_settings().config)


if __name__ == '__main__':
    start()
