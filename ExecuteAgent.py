import anthropic

API_KEY = "ms-64ca6039-9321-47de-94b4-028b6ebddcb7"
BASE_URL = "https://api-inference.modelscope.cn"
MODE_ID = "Qwen/Qwen2.5-7B-Instruct"

client = anthropic.Client(api_key=API_KEY, base_url=BASE_URL)

messages = client.messages.create(model= MODE_ID,
                       messages=[{"role": "user", "content": "查询杭州明天的天气"}],
                       max_tokens= 1024)
print(messages.content[0].text)