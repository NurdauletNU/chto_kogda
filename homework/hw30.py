# 1.	Сверстать страницу для отображения текущей погоды и парсить погоду через requests с любого сайта

import requests


def get_weather_now(url):
    headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
}

    responce=requests.get(url=url)
    data=responce.text
    data1=data.split('class="temp fact__temp fact__temp_size_s')[1].split('class="temp__value temp__value_with-unit')[1].split('">')[1].split("<")[0]
    return f"Текущая погода {data1}"

print(get_weather_now(url="https://yandex.kz/pogoda/karaganda"))
