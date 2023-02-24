from env_profile.base import BaseSetting


class Setting(BaseSetting):
    config = {
        "host": "0.0.0.0",
        "port": 7401
    }
    open_aic_api_key = "open_aic_api_key"