
from pydantic import BaseSettings
import os


class BaseSetting(BaseSettings):
    static_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + '/static/'
    root_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
