from bot.bot import Bot
import openai
import os


class OpenAIBot(Bot):
    def __init__(self):
        openai.api_key = os.environ['VITE_OPENAI_API_KEY']

    def reply(self, query):
        success, reply_content = self.reply_text(query)
        return success, reply_content

    def reply_text(self, content):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{'role': "user", "content": content}]
            )
            res_content = response['choices'][0]['message']['content'].strip()
            return True, res_content
        except openai.error.RateLimitError as e:
            # rate limit exception
            return False, "提问太快啦，请休息一下再问我吧"
        except Exception as e:
            return False, "请再问我一次吧"