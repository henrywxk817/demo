from bot.open_ai_bot import OpenAIBot


"""
channel factory
"""


def create_bot():
    """
    create a channel instance
    :param channel_type: channel type code
    :return: channel instance
    """
    return OpenAIBot()
