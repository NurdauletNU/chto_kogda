import requests

response=requests.get("https://jsonplaceholder.typicode.com/todos")
answer=response.json()
# print(answer)


def example():
    response1=requests.get("https://www.mig.kz/")
    data1=response1.text
    data1=data1.split('<td class="buy delta-neutral">')[1]
    print(data1.split("</td>")[0])


headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
}

response = requests.get('https://shop.kz/videokarty/filter/almaty-is-v_nalichii-or-ojidaem-or-dostavim/apply/', headers=headers)
data = response.text
data1 = data.split('class="bx-catalog-product-middle"')[1:]
export = []
for i in data1:
    try:
        # print('\n\n\n\n')
        title = i.split('title="')[1].split('">')[0]
        # print(type(title), title)

        price1 = i.split('<span class="old_price">')[1].split('<div class="you_save">')[0].split('</span>')[1].strip()
        price2 = float(price1[:-1].replace(' ', ''))
        # print(type(price2), price2)
        export.append({f"{title}": price2})
    except:
        pass

for i in export:
    print(i)