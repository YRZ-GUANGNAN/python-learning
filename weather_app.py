import json
import datetime
import requests
from config import api_key

HISTORY_FILE = "history.json"


# ══════════════ 工具函数 ══════════════

def load_history():
    """读取历史记录。文件不存在时返回空列表。"""
    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def save_history(history):
    """把历史记录写进文件。"""
    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(history, f, ensure_ascii=False)


def get_weather(city_name):
    """查询城市天气。成功返回数据，失败返回 None。"""
    geo_url = f"https://restapi.amap.com/v3/geocode/geo?key={api_key}&address={city_name}"
    geo_response = requests.get(geo_url, timeout=5)
    geo_data = geo_response.json()

    if geo_data["status"] != "1" or geo_data["count"] == "0":
        return None

    adcode = geo_data["geocodes"][0]["adcode"]

    weather_url = f"https://restapi.amap.com/v3/weather/weatherInfo?key={api_key}&city={adcode}"
    weather_response = requests.get(weather_url, timeout=5)
    weather_data = weather_response.json()

    live = weather_data["lives"][0]

    return {
        "city": live["city"],
        "weather": live["weather"],
        "temperature": live["temperature"],
        "humidity": live["humidity"],
    }


def show_menu():
    print()
    print("=== 天气查询工具 ===")
    print("1. 查询天气")
    print("2. 查看查询历史")
    print("3. 清空历史")
    print("4. 退出")


def show_history():
    history = load_history()

    if len(history) == 0:
        print("还没有查询记录")
    else:
        print("\n查询历史：")
        for record in history:
            print(f"{record['time']}  {record['city']}  {record['weather']}  {record['temperature']}℃")


# ══════════════ 主程序 ══════════════

while True:
    show_menu()
    choice = input("请选择：")

    if choice == "1":
        city = input("请输入城市名：")
        result = get_weather(city)

        if result is None:
            print("查不到这个城市")
        else:
            print(f"城市：{result['city']}")
            print(f"天气：{result['weather']}")
            print(f"温度：{result['temperature']}℃")
            print(f"湿度：{result['humidity']}%")

            result["time"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

            history = load_history()
            history.append(result)
            save_history(history)

    elif choice == "2":
        show_history()

    elif choice == "3":
        save_history([])
        print("历史已清空")

    elif choice == "4":
        print("再见")
        break

    else:
        print("请输入 1-4 之间的数字")

    input("\n按回车继续...")