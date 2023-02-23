
from pydantic import BaseModel
from typing import Any


class BaseRes(BaseModel):
    code: str = 200
    status: int = 1
    data: Any = ''
    error: str = ''
