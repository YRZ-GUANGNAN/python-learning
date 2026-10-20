import json
import requests
from config import deepseek_key

url = "https://api.deepseek.com/chat/completions"

headers = {
    "Authorization": f"Bearer {deepseek_key}",
}

body = {
    "model": "deepseek-chat",
    "messages": [
        {"role": "user", "content": "你叫什么名字？"}
    ],
}

response = requests.post(url, headers=headers, json=body, timeout=30)

data = response.json()

if "error" in data:
    print("调用失败：", data["error"]["message"])
else:
    print("AI 说：", data["choices"][0]["message"]["content"])