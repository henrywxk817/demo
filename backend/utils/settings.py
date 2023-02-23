
config = None


def get_settings(env=None):
    global config
    if config is not None:
        return config
    if env == 'local':
        from env_profile.local import Setting as Config
    elif env == 'prod':
        from env_profile.prod import Setting as Config
    else:
        from env_profile.local import Setting as Config
    config = Config()
    return config

