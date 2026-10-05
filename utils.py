# a520ee48de948b4f702419e3b19ddec3

# import requests
#
# api_key = ""
# code_city = input("请输入你的城市编号：")
# url = f"https://restapi.amap.com/v3/weather/weatherInfo?key={api_key}&city={code_city}"
#
# response = requests.get(url, timeout=5)
# data = response.json()
#
# live = data["lives"][0]      # ← 先取出那一条（一个字典），起名叫 live
#
# print(f"城市：{live['city']}")
# print(f"天气：{live['weather']}")
# print(f"温度：{live['temperature']}℃")

# import requests
#
# api_key = "a520ee48de948b4f702419e3b19ddec3"
#
# url = f"https://restapi.amap.com/v3/geocode/geo?key={api_key}&address=北京市"
#
# response = requests.get(url, timeout=5)
#
# print(response.text)
#
# import requests
#
# from config import api_key
#
# city_name = input("请输入城市名：")
#
# # ═══ 第一步：城市名 → adcode ═══
# geo_url = f"https://restapi.amap.com/v3/geocode/geo?key={api_key}&address={city_name}"
#
# geo_response = requests.get(geo_url, timeout=5)
# geo_data = geo_response.json()
#
# adcode = geo_data["geocodes"][0]["adcode"]
#
#
# # ═══ 第二步：adcode → 天气 ═══
# weather_url = f"https://restapi.amap.com/v3/weather/weatherInfo?key={api_key}&city={adcode}"
#
# weather_response = requests.get(weather_url, timeout=5)
# weather_data = weather_response.json()
#
# live = weather_data["lives"][0]
#
# print(f"城市：{live['city']}")
# print(f"天气：{live['weather']}")
# print(f"温度：{live['temperature']}℃")

print("我是实验分支")
import requests
from config import api_key

city_name = input("请输入城市名：")

# ═══ 第一步：城市名 → adcode ═══
geo_url = f"https://restapi.amap.com/v3/geocode/geo?key={api_key}&address={city_name}"

geo_response = requests.get(geo_url, timeout=5)
geo_data = geo_response.json()

if geo_data["status"] != "1" or geo_data["count"] == "0":
    print("查不到这个城市，请检查名字是否正确")
else:
    adcode = geo_data["geocodes"][0]["adcode"]

    # ═══ 第二步：adcode → 天气 ═══
    weather_url = f"https://restapi.amap.com/v3/weather/weatherInfo?key={api_key}&city={adcode}"

    weather_response = requests.get(weather_url, timeout=5)
    weather_data = weather_response.json()

    live = weather_data["lives"][0]

    print(f"城市：{live['city']}")
    print(f"天气：{live['weather']}")
    print(f"温度：{live['temperature']}℃")
    print(f"湿度：{live['humidity']}%")