from fastapi import APIRouter, Body
from response_model.base_resm import BaseRes
from utils.logger import logger
from bot import bot_factory
import traceback

router = APIRouter()


@router.post('/correction/', response_model=BaseRes)
def correction(content: str = Body(..., embed=True)) -> BaseRes:
    try:
        response = bot_factory.create_bot().reply("修改错别字: " + content)
        return BaseRes(data=response)
    except Exception as e:
        logger.error(e)
        logger.error(traceback.format_exc())
        return BaseRes(status=0, error=str(e))