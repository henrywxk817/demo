from bot.bot import Bot
from utils.logger import logger
import openai
import os


class OpenAIBot(Bot):
    def __init__(self):
        openai.api_key = os.environ['VITE_OPENAI_API_KEY']

    def reply(self, query):
        logger.debug("[OPEN_AI] session query={}".format(query))
        success, reply_content = self.reply_text(query)
        logger.debug("[OPEN_AI] query={}, reply_cont={}".format(query, reply_content))
        return success, reply_content

    def reply_text(self, content):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{'role': "user", "content": content}]
            )
            res_content = response['choices'][0]['message']['content'].strip()
            prompt_tokens = response['usage']['prompt_tokens']
            completion_tokens = response['usage']['completion_tokens']
            total_tokens = response['usage']['total_tokens']
            logger.info(
                f"[OPEN_AI] prompt_tokens={prompt_tokens} completion_tokens={completion_tokens} total_tokens={total_tokens}")
            logger.debug("[OPEN_AI] reply={}".format(res_content))
            return True, res_content
        except openai.error.RateLimitError as e:
            # rate limit exception
            logger.error(e)
            return False, "提问太快啦，请休息一下再问我吧"
        except Exception as e:
            logger.exception(e)
            return False, "请再问我一次吧"