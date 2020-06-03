# 중고차 사이트에서 자료를 읽고 중고차 정보, 가격을 DataFrame으로 출력. 평균이랑 표준편차도 출력
import urllib.request as req
from bs4 import BeautifulSoup
from pandas import DataFrame

carurl = "https://www.bobaedream.co.kr/mycar/mycar_list.php?gubun=K"
car = req.urlopen(carurl)
# print(car)

soup = BeautifulSoup(car, 'lxml')
info = soup.select('#listCont > div.wrap-thumb-list > ul > li > div')
datas = []

for i in info:
    name = i.select('div.mode-cell.title > p > a')[0].text
    year = i.select('div.mode-cell.year > span')[0].text
    fuel = i.select('div.mode-cell.fuel > span')[0].text
    km = i.select('div.mode-cell.km > span')[0].text
    tempPrice = i.select('div.mode-cell.price > b > em')[0].text
    price = ''
    for p in tempPrice:
        try:
            int(p)
            price += p
            # print(price)
        except:
            pass
    datas += [[name, year, fuel, km, int(price)]]

df1 = DataFrame(datas, columns=['이름', '연식', '연료', '주행', '가격'])
print(df1.head())
print('가격 평균 : ', df1['가격'].mean())
print('가격 표준편차 : ', df1['가격'].std())

