import requests
from config import deepseek_key

url = "https://api.deepseek.com/chat/completions"

# 请求头：身份验证（字典）
headers = {
    "Authorization": f"Bearer {deepseek_key}",
}

# 消息列表：对话内容（列表），放在循环外面才能累积
messages = [
    {"role": "system", "content": "你是一个简洁的助手，回答尽量简短"}
]

while True:
    question = input("你：")

    if question == "退出":
        break

    messages.append({"role": "user", "content": question})

    body = {
        "model": "deepseek-chat",
        "messages": messages,
    }

    response = requests.post(url, headers=headers, json=body, timeout=30)
    data = response.json()

    if "error" in data:
        print("调用失败：", data["error"]["message"])
        break

    answer = data["choices"][0]["message"]["content"]
    print("AI：", answer)

    messages.append({"role": "assistant", "content": answer})