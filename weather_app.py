import requests
from config import api_key



def get_weather(city_name):
    """查询城市天气。成功返回数据，失败返回 None。"""
    # —— 第一步：城市名 -- adcode ——
    geo_url = f"https://restapi.amap.com/v3/geocode/geo?key={api_key}&address={city_name}"

    geo_response = requests.get(geo_url,timeout=5)
    geo_data = geo_response.json()

    if geo_data["status"] != "1" or geo_data["count"] == "0":
        return None

    adcode = geo_data["geocodes"][0]["adcode"]

    # ———— 第二步；adcode ———— 天气 ————
    weather_url =f"https://restapi.amap.com/v3/weather/weatherInfo?key={api_key}&city={adcode}"

    weather_response =requests.get(weather_url,timeout=5)

    weather_data =weather_response.json()

    live = weather_data["lives"][0]

    return{
        "city":live["city"],
        "weather": live["weather"],
        "temperature":live["temperature"],
        "humidity":live["humidity"]

    }
city = input("请输入城市名：")

result = get_weather(city)

if result is None:
    print("查不到这个城市")
else:
    print(f"城市：{result['city']}")
    print(f"天气：{result['weather']}")
    print(f"温度：{result['temperature']}℃")
    print(f"湿度：{result['humidity']}%")
