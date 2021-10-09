# Before run script, you need to create 2 files : pays.csv and urls.txt

import requests
from bs4 import BeautifulSoup
import time


links = []
for i in range(26):
    url = 'http://example.python-scraping.com/places/default/index/' + str(i)
    response = requests.get(url)
    if response.ok:
        soup = BeautifulSoup(response.text, 'lxml')
        tds = soup.findAll('td')
        for td in tds:
            a = td.find('a')
            link = a['href']
            links.append('http://example.python-scraping.com' + link)
        time.sleep(1)

with open('urls.txt', 'w') as file:
    for link in links:
        file.write(link + '\n')

with open('urls.txt', 'r') as inf:
    with open('pays.csv', 'w') as outf:
        outf.write('pays,population\n')
        for row in inf:
            print(row)
            url = row.strip()
            response = requests.get(url)
            if response.ok:
                soup = BeautifulSoup(response.text, 'lxml')
                country = soup.find('tr', {'id' : 'places_country_or_district__row'}).find('td', {'class':'w2p_fw'})
                pop = soup.find('tr', {'id' : 'places_population__row'}).find('td', {'class':'w2p_fw'})
                print('Pays: ' + country.text + ', Population: ' + pop.text)
                outf.write(country.text + "," + pop.text.replace(",","") + '\n')
            time.sleep(1)