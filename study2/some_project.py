import aiohttp
import requests


class Valute():
    def __init__(self,name:str, symbol:str, priceUSD:float):
        self.priceUSD = priceUSD
        self.symbol = symbol
        self.name = name


async def async_t(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) '
                      'Chrome/102.0.0.0 Safari/537.36'
    }
    async with aiohttp.ClientSession as session:
        async with session.get(url=url,headers=headers) as response:
            data=await response.read()
            return data


def get_valutes(url:str, locale:str, filter_by_price:float)-> list[Valute]:
    """
    Декомпозиция:
    1. Получить данные с сайта
    2. Отфильтровать данные по параметрам(search, filter_q)
    3. Сериализация(JSON->PYTHON OBJECT)
    """
    url=f"{url}&locale={locale}"
    data=requests.get(url).json()
    print(data)
    pass


if __name__=="__main__":
    get_valutes(url="https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false",
                locale="ru", filter_by_price="")