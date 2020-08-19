import requests
import bs4
import sys
import codecs
import json
import csv
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
url = 'https://minimini.jp/list/pref/tokyo/chofushi/?lnkdiv=6&SortKBN=5&ListNum=5'


def get_data(url):
    print(url)
    html = requests.get(url, headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}).text
    data = []
    # with open('data/source3.html', 'rt', encoding='utf-8') as f:
    #     html = f.read()
    doc = bs4.BeautifulSoup(html, 'html.parser')
    for bukken in doc.select('.bukken'):
        tateya_table = bukken.select_one('.tateya_table')
        chikunen = tateya_table.select_one('td:nth-of-type(2)').get_text()
        year = int(chikunen[:chikunen.find('年')])
        month = int(chikunen[chikunen.find('年')+1:chikunen.find('月')])
        when = year*12+month
        station = tateya_table.select('td')[2].get_text()
        walk = int(station[station.find('徒歩')+2:station.find('分', station.find('徒歩'))])

        madori = str(bukken.select_one('.room_table td.madori'))
        menseki = float(madori[madori.find('<br/>')+5:madori.find('m', madori.find('<br/>'))])

        kaisu = str(bukken.select_one('.room_table td.kaisu'))
        kaisu_num = int(kaisu[kaisu.find('<br/>')+5:kaisu.find('階', kaisu.find('<br/>'))])

        yachin = float(bukken.select_one('.room_table td.chiryo > strong').get_text())

        # data.append({
        #     'when': when,
        #     'walk': walk,
        #     'menseki': menseki,
        #     'kaisu': kaisu_num,
        #     'yachin': yachin
        # })
        data.append([when, walk, menseki, kaisu_num, yachin])
    return data


data = []
i = 1
while True:
    # try:
        data.extend(get_data(url+'&dp='+str(i)))
        i += 1
    # except Exception as ex:
    #     print(ex)
    #     break


with open('data/data1.csv', 'wt', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['when', 'walk', 'menseki', 'kaisu', 'yachin'])
    for d in get_data(url):
        writer.writerow(d)
    # json.dump(get_data(url), f)
