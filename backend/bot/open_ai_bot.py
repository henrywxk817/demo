from bot.bot import Bot
import openai
import os


class OpenAIBot(Bot):
    def __init__(self):
        openai.api_key = os.environ['VITE_OPENAI_API_KEY']

    def ask(self, content):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{'role': "user", "content": content}]
            )
            res_content = response['choices'][0]['message']['content'].strip()
            return True, res_content
        except openai.error.APIConnectionError:
            # api connection exception
            return False, "我连接不到你的网络"
        except openai.error.Timeout:
            return False, "我没有收到你的消息"
        except openai.error.RateLimitError:
            # rate limit exception
            return False, "提问太快啦，请休息一下再问我吧"
        except Exception as e:
            return False, "请再问我一次吧"

    def ask_stream(self, messages):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages
            )
            res_content = response['choices'][0]['message']['content'].strip()
            return True, res_content
        except openai.error.APIConnectionError:
            # api connection exception
            return False, "我连接不到你的网络"
        except openai.error.Timeout:
            return False, "我没有收到你的消息"
        except openai.error.RateLimitError:
            # rate limit exception
            return False, "提问太快啦，请休息一下再问我吧"
        except Exception as e:
            return False, "请再问我一次吧"