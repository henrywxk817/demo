from fastapi import APIRouter, Body, Request
from response_model.base_resm import BaseRes
from bot import bot_factory
from slowapi import Limiter
from slowapi.util import get_remote_address

router = APIRouter()
limiter = Limiter(key_func=get_remote_address)


@router.post('/correction/', response_model=BaseRes)
# @limiter.limit("1/second")
def correction(content: str = Body(..., embed=True)) -> BaseRes:
    try:
        success, response = bot_factory.create_bot().reply(content)
        return BaseRes(data={"success": success, "response": response})
    except Exception as e:
        return BaseRes(status=0, error=str(e))


@router.post('/ask_stream/', response_model=BaseRes)
def ask_stream(messages: dict = Body(..., embed=True)) -> BaseRes:
    try:
        success, response = bot_factory.create_bot().ask_stream(messages)
        return BaseRes(data={"success": success, "response": response})
    except Exception as e:
        return BaseRes(status=0, error=str(e))