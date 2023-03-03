
from pydantic import BaseSettings
import os


class BaseSetting(BaseSettings):
    root_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
