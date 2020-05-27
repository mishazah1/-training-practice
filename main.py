import requests
from bs4 import BeautifulSoup



URL = 'https://coinmarketcap.com/'
valutes = []


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    itemsN = soup.find_all('tr', class_='cmc-table-row')
    itemsM = soup.find_all('td', class_='cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__market-cap')
    itemsP = soup.find_all('td', class_='cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__price')

    for itemN,itemM,itemP in zip(itemsN, itemsM, itemsP):
        valutes.append({
            'Name': itemN.find('a', class_='cmc-link').get_text(strip=True),
            'Market_cap': itemM.find('div').get_text(strip=True),
            'Price': itemP.find('a', class_='cmc-link').get_text(strip=True)
        })

    return(valutes)


def search(Name, valutes):

    return next((item for item in valutes if item.get("Name") and item["Name"] == Name),None)

def parse():
    max_pages = 26
    pages = []
    for x in range(1, max_pages + 1):
        pages.append(requests.get(URL + str(x)))

    for r in pages:
        html = r


        get_content(html.text)

    print("Введите название криптовалюты")
    print('Чтобы закончить работу программы,введите "Выход":')

    while(1):

        s = input()
        if(s!='Выход'):
            if (search(s, valutes))!=None:
                print(search(s, valutes))
            else:
                print('Запись не найдена')
        else:
            break


parse()