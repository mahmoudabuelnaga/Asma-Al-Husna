from bs4 import BeautifulSoup
import csv
import requests

endpoints = f"https://www.islamicreliefcanada.org/resources/99-names-of-allah/"

get_response = requests.get(endpoints)

soup = BeautifulSoup(get_response.content, 'lxml')

section = soup.find('tbody')

items = []    
tr = [i.text for i in section.find_all('td')]
number = [tr[i] for i in range(0,len(tr),4)]
name = [tr[i] for i in range(1,len(tr),4)]
transliteration = [tr[i] for i in range(2,len(tr),4)]
meaning = [tr[i] for i in range(3,len(tr),4)]

for number, name, transliteration, meaning in zip(number, name, transliteration, meaning):
    item = {}
    item['number'] = number
    item['name'] = name
    item['transliteration'] = transliteration
    item['meaning'] = meaning

    items.append(item)


filename = f'/home/naga/dev/scraping/Asma-Al-Husna/asma_al_husna.csv'
with open(filename, 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=['number','name','transliteration','meaning'], extrasaction='ignore' , delimiter = ';')
    w.writeheader()
    for item in items:
        w.writerow(item)
        print(item)
