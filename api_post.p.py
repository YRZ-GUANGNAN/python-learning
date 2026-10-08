import requests

data = {"name": "张三", "age": 18}

try:
    response = requests.post(
        "https://httpbin.org/post",
        json=data,
        timeout=10,
    )
    print("状态码：", response.status_code)
    print(response.text)

except requests.RequestException as e:
    print("连不上：", e)