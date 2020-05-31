# BBQ 사이트 자료 읽고 메뉴와 가격 출력. 가격의 평균, 표준편차
import urllib.request as req
import bs4

bbqurl = "https://www.bbq.co.kr/menu/menuList.asp"
bbq = req.urlopen(bbqurl)
print(bbq)

soup = bs4.BeautifulSoup(bbq, 'lxml')
data1 = soup.select('div.box > div.info > p.name')  # 메뉴명
data2 = soup.select('div.box > div.info > p.pay')  # 가격

name = []
pay = []
for a in data1:
    name.append(a.text)  # list에 메뉴명을 저장

print(name)

for b in data2:  # replace : 데이터를 가공할 때 씀
    pay.append(int(b.text.replace(',', '').replace('원', '')))  # list에 가격을 저장. ','가 있는 녀석은 지우고 '원'도 지운다.

print(pay)

data = {'name': name, 'pay': pay}

from pandas import DataFrame
df = DataFrame(data)
print(df)

print('\n=========================\n')
bbqurl2 = "https://www.bbq.co.kr/menu/menuList.asp"
bbq2 = req.urlopen(bbqurl2)
soup = bs4.BeautifulSoup(bbq2, 'lxml')
datas = []
info = soup.select('div.info')
# print('info : ', info)

for i in info:
    tempPrice = i.select('p.pay')[0].text
    price = ''
    for j in tempPrice:  # 19,000원
        try:
            int(j)
            price += j  # 정수 하나하나 꺼내서 더하기       1 19 190 1900...
            print(price)
        except:
            pass
    datas += [[i.select('p.name')[0].text, int(price)]]

df2 = DataFrame(datas, columns=['메뉴', '가격'])
print(df2.head())
print('가격 평균 : ', df2['가격'].mean())
print('가격 표준편차 : ', df2['가격'].std())
