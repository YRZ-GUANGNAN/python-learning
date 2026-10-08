import json
import requests
from config import deepseek_key

url = "https://api.deepseek.com/chat/completions"
CHAT_FILE = "chat_history.json"

headers = {
    "Authorization": f"Bearer {deepseek_key}",
}

SYSTEM_PROMPT = {"role": "system", "content": "你是一个简洁的助手，回答尽量简短"}


def load_chat():
    """读取对话记录。文件不存在时返回空列表。"""
    try:
        with open(CHAT_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def save_chat(messages):
    """把对话记录写进文件。"""
    with open(CHAT_FILE, "w", encoding="utf-8") as f:
        json.dump(messages, f, ensure_ascii=False, indent=2)


def show_menu():
    print()
    print("=== AI 助手 ===")
    print("1. 开始新对话")
    print("2. 继续上次的对话")
    print("3. 查看对话记录")
    print("4. 退出")


def show_chat():
    """查看对话记录。← 这个你来写"""
    messages = load_chat()

    if len(messages) == 0:
        print("还没有对话记录")
    else:
        for msg in messages:
            if msg["role"] == "user":
                print(f"你：{msg['content']}")
            elif msg["role"] == "assistant":
                print(f"AI：{msg['content']}")


def chat(messages):
    """进入对话循环。"""
    while True:
        question = input("你：")

        if question == "退出":
            break

        messages.append({"role": "user", "content": question})

        body = {"model": "deepseek-chat", "messages": messages}
        response = requests.post(url, headers=headers, json=body, timeout=30)
        data = response.json()

        if "error" in data:
            print("调用失败：", data["error"]["message"])
            break

        answer = data["choices"][0]["message"]["content"]
        print("AI：", answer)

        messages.append({"role": "assistant", "content": answer})
        save_chat(messages)


while True:
    show_menu()
    choice = input("请选择：")

    if choice == "1":
        messages = [SYSTEM_PROMPT]
        save_chat(messages)
        print("（新对话）")
        chat(messages)

    elif choice == "2":
        messages = load_chat()
        if len(messages) == 0:
            print("还没有对话记录")
        else:
            chat(messages)

    elif choice == "3":
        show_chat()

    elif choice == "4":
        print("再见")
        break

    else:
        print("请输入 1-4 之间的数字")

    input("\n按回车继续...")