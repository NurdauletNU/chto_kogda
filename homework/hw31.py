# 2.	Сверстать страницу для отображения текущего курса валют и парсить данные через requests + bs4  с любого сайта

import requests
from bs4 import BeautifulSoup
url="https://www.mig.kz/"
response=requests.get(url=url).text
data=BeautifulSoup(response, "html.parser")
data1=data.find("td",class_="buy delta-neutral")
data2=data1.text
print(f'Покупка долара вам обойдется в {data2} тенге')


