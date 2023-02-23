import requests
import json

import openai
from utils.settings import get_settings



# data = {"content": '实际上，从2022年开始，她所在幼儿园就开始直面招式难，今年生源可能进一步下滑。'}
# res = requests.post(url="http://localhost:7401/api/v1/chatGPT/correction", data=json.dumps(data))
# print(res.text)


query = "实际上，从2022年开始，她所在幼儿园就开始直面招升难，今年生源可能进一步下滑。"
openai.api_key = get_settings().open_aic_api_key
response = openai.Edit.create(
    model="text-davinci-edit-001",  # 对话模型的名称
    input=query,
    instruction='修改错别字')
res_content = response["choices"][0]["text"].strip().replace('<|endoftext|>', '')
print(res_content)

