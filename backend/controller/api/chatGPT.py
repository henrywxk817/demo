from fastapi import APIRouter, Body
from response_model.base_resm import BaseRes
from bot import bot_factory

router = APIRouter()


@router.post('/correction/', response_model=BaseRes)
def correction(content: str = Body(..., embed=True)) -> BaseRes:
    try:
        success, response = bot_factory.create_bot().reply(content)
        return BaseRes(data={"success": success, "response": response})
    except Exception as e:
        return BaseRes(status=0, error=str(e))