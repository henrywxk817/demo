from bot.bot import Bot
from utils.logger import logger
import openai
import time
from utils.settings import get_settings


class OpenAIBot(Bot):
    def __init__(self):
        openai.api_key = get_settings().open_aic_api_key

    def reply(self, query):
        # acquire reply content
        logger.debug("[OPEN_AI] query={}".format(query))
        reply_content = self.reply_text(query, 0)
        return reply_content

    def reply_text(self, query, retry_count=0):
        try:
            response = openai.Edit.create(
                    model="text-davinci-edit-001",
                    input=query,
                    instruction='修改错别字')
            res_content = response.choices[0]['text'].strip().replace('<|endoftext|>', '')
            logger.info("[OPEN_AI] reply={}".format(res_content))
            return res_content
        except openai.error.RateLimitError as e:
            # rate limit exception
            logger.error(e)
            if retry_count < 1:
                time.sleep(5)
                logger.error("[OPEN_AI] RateLimit exceed, 第{}次重试".format(retry_count+1))
                return self.reply_text(query, retry_count+1)
            else:
                return "提问太快啦，请休息一下再问我吧"
        except Exception as e:
            # unknown exception
            logger.exception(e)
            return "请再问我一次吧"