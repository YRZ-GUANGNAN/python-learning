import requests

try:
    response = requests.get("https://github.com", timeout=10)
    print("状态码：", response.status_code)
except requests.RequestException as e:
    print("连不上：", e)
