# 위키백과 자료 읽기
import urllib.request as req
from bs4 import BeautifulSoup

url = "https://ko.wikipedia.org/wiki/%EC%9D%B4%EC%88%9C%EC%8B%A0"
wiki = req.urlopen(url)
soup = BeautifulSoup(wiki, 'lxml')
# print(soup)
#   #mw-content-text > div > p:nth-child(6)
# print(soup.select_one('#mw-content-text > div > p'))    # p태그만 읽어서 가져온다.    select를 하면 전체를 불러온다.

print('=========================')
daumurl = 'https://news.v.daum.net/v/20200528120811852'
daum = req.urlopen(daumurl)

print(daum)  # <http.client.HTTPResponse object at 0x1097bcd50>
soup = BeautifulSoup(daum, 'lxml')
# print(soup)
print(soup.select_one('div#kakaoIndex > a').string)  # kakaoIndex라는 id를 가진 div태그의 value 한 개를 가져옴 - '본문 바로가기'
datas = soup.select('div#kakaoIndex > a')
# print(datas)  # [<a href="#kakaoBody">본문 바로가기</a>, <a href="#kakaoGnb">메뉴 바로가기</a>]

for i in datas:
    # print(i)
    href = i.attrs['href']
    text = i.string
    print('href : {}, text : {}'.format(href, text))

print('\n원하는 문단 가져오기-------------------------------')
#harmonyContainer > section > p:nth-child(5)    # 내가 원하는 문단을 사이트에서 선택 후 오른쪽 클릭 눌러서 selector 가져옴.
datas3 = soup.select('#harmonyContainer > section > p')
print(datas3)

# for i in datas3:
# for i in datas3[:3]:  # 3개의 p태그만 가져온다.
for i in datas3[2:3]:   # 2번째 p태그부터 3태그를 가져온다.
    print(i.string)