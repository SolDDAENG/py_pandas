# naver 사이트의 영화 순위 읽기
from bs4 import BeautifulSoup

# 방법 1
print('=======방법 1=========')
import urllib.request

url = "https://movie.naver.com/movie/sdb/rank/rmovie.nhn"
data = urllib.request.urlopen(url).read()
soup = BeautifulSoup(data, 'lxml')
# print(soup)
# print(soup.select('div.tit3'))
# print(soup.select('div[class=tit3]'))
for tag in soup.select('div[class=tit3]'):
    print(tag.text.strip())  # strip : 앞 뒤 공백 제거

# 방법 2
print('---------방법 2--------')
import requests

data = requests.get("https://movie.naver.com/movie/sdb/rank/rmovie.nhn")
# print(data.status_code, ' ', data.encoding)    # 정보를 얻을 수 있음.    200    MS949
# datas = data.text    # read대신 text사용
# print(datas)

datas = requests.get("https://movie.naver.com/movie/sdb/rank/rmovie.nhn").text
soup = BeautifulSoup(datas, 'lxml')
# print(soup)
# m_list = soup.findAll("div", tit3")    # ("엘리먼트명", "속성")    # 가독성이 떨어짐
m_list = soup.findAll("div", {"class": "tit3"})  # 가독성을 위해서 이렇게 적어주자
# print(m_list)   # <a href="/movie/bi/mi/basic.nhn?code=193992" title="런 보이 런">런 보이 런</a>

# 참고-----------------------------------------
title = 'abcdefg'
print(title[title.find('b'):title.find('f')])
# --------------------------------------------

for i in m_list:
    # print(i)
    title = i.findAll('a')
    print(str(title)[
          str(title).find('title=" ') + 7:str(title).find(' ">')])  # title까지가 7글자이다. ' ">' 가 나오기 전까지 출력 --> 영화제목

print('-----순위 표시-----')
count = 1
for i in m_list:
    title = i.find('a')
    print(str(count) + "위 : " + title.string)
    count += 1
