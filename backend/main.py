
import os
from utils.settings import get_settings

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from controller.api.chatGPT import router as chatGPT_route, limiter as chatGPT_limiter
import uvicorn
from slowapi.errors import RateLimitExceeded
from slowapi import _rate_limit_exceeded_handler


def create_app() -> FastAPI:
    app = FastAPI()
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
    app.state.limiter = chatGPT_limiter
    app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
    return app


app = create_app()


def start():
    global app
    uvicorn.run("main:app", **get_settings().config)


if __name__ == '__main__':
    start()
