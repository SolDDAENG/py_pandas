# HTML/XML 전용 처리 모튤 : BeautifulSoup
from bs4 import BeautifulSoup

html_data = '''
<html><body>
<h1>뷰티플 라이프</h1>
<p>웹 페이지 분석</p>
<p>원하는 자료 추출</p>
</body></html>
'''

# print(html_data, type(html_data))   # <class 'str'>
soup = BeautifulSoup(html_data, 'html.parser')
# html.parser : HTML 문법 규칙에 따른 문자열을, 해당 문법을 바탕으로 단어의 의미나 구조를 분석하는 것. 빠르지만 유연하지 않아 단순한 html문서에 사용한다.
print(soup, type(soup))  # <class 'bs4.BeautifulSoup'>

print()
h1 = soup.html.body.h1  # BeautifulSoup는 속성 명령어를 사용할 수 있다.
p1 = soup.html.body.p
p2 = p1.next_sibling.next_sibling  # next_sibling : 그 다음 태그에 접근. # p1태그의 다음 태그 <p>와 그 다음 태그 </p>
print(h1, ' ', h1.string)  # <h1>뷰티풀 라이플</h1>   뷰티풀 라이플
print(p1, ' ', p1.string)  # <p>웹 페이지 분석</p>   웹 페이지 분석
print(p2, ' ', p2.string)  # <p>원하는 자료 추출</p>   원하는 자료 추출

print('\n===========================================================================')
html_data2 = '''
<html><body>
<h1 id = "title">뷰티풀 라이플</h1>
<p>웹 페이지 분석</p>
<p id = "my">원하는 자료 추출</p>
</body></html>
'''

soup2 = BeautifulSoup(html_data2, 'lxml')
# print(soup2, type(soup2))
print(soup2.p, soup2.p.string)  # lxml : BeautifulSoup에서 지원하는 parser. 빠르고 유연하다.
print(soup2.find('p'), soup2.find('p').string)
print(soup2.find('p', id='my'), soup2.find('p', id='my').string)  # find(태그명, id명)
print(soup2.find(id='title').string)  # find() : id속성만으로도 찾을 수 있다.
print(soup2.find(id='my').string)  # find() : id속성만으로도 찾을 수 있다.

print("\n***************************************************************************")
html_data3 = '''
<html><body>
<h1 id="title">뷰티플 라이프</h1>
<p>웹 페이지 분석</p>
<p id="my">원하는 자료 추출</P>
<div>
    <a href="http://www.naver.com">naver</a>
    <a href="http://www.google.com">google</a>
</div>
</body></html>
'''

soup3 = BeautifulSoup(html_data3, 'lxml')
# print(soup3)  # BeautifulSoap 객체
# print(soup3.prettify())     # 들여쓰기를 자동으로 해서 이쁘게 본다.
print(soup3.find('a'), ' ', soup3.find('a').string)  # Element명 : a
print(soup3.find(['a']))  # 이렇게도 가능은 하다.
print(soup3.find_all(['a']))  # find_all() : 여러개를 찾는다.
print(soup3.findAll('a'))  # find_all을 findAll()로 쓸 수 있다. []괄호는 의미없음. list형태로 저장
links = soup3.find_all('a')
print(links)

for i in links:
    href = i.attrs['href']  # href의 속성을 얻음.
    text = i.string
    print(href, ' ', text)

print(soup3.find_all('p'))
print(soup3.find_all(['p', 'h1']))  # 여러가지 태그도 복수로 선택 할 수 있다.
aa = soup3.find_all(string=['뷰티플 라이프', '웹 페이지 분석', '원하는 자료 추출'])  # string을 항목으로 검색
print(aa)

print('\n정규 표현식 가능=========================================')
import re

link2 = soup3.findAll(href=re.compile(r'^ht'))  # 첫 글자가 ht로 시작하는 href속성을 찾는다.
print(link2)
for h in link2:
    print(h.attrs['href'])  # 속성값 추출

print('\n\n Css selector 이용 ==================')
html_data4 = '''
<html><body>
<div id="hello">
    <a href="http://www.naver.com">naver</a>
    <span>
        <i>
            <a href="http://www.asia.com">asia</a>        
        </i>        
        <a href="http://www.korea.com">korea</a>
    </span>
    <ul class="world">
        <li>안녕</li>
        <li>디지몬</li>
    </ul>
    <ul class="end">
        <li>너와</li>
        <li>함께하고 싶어</li>
    </ul>
</div>
<div id="sbs">
    <b>찾아라 비밀의 열쇠</b>
    <a href="http://www.google.com">google</a>
</div>
</body></html>
'''
soup4 = BeautifulSoup(html_data4, 'lxml')
# a = soup4.select_one('div a')     # div태그 안의 a ==> 처음 나오는 div의 a태그 => naver.com
a = soup4.select_one('div#sbs a')  # id가 sbs인 div태그 안의 a => www.google.com
print('a : ', a)

b = soup4.select_one('div#hello a')  # naver
print('b : ', b)

c = soup4.select_one('div#hello span > a').string
# korea : hello란 id를 가진 dix태그 안에 span태그 안에 있는 '직계자식' 태그
# '>'는 가장 먼저 나오는 직계자식
print(c)

d = soup4.select_one('div#hello span a').string     # asia : hello란 id를 가진 div태그 안에 span태그 안에 있는 a태그의 value
print(d)

print()
e = soup4.select('div#hello ul.world > li') # '.'은 클래스. '>'는 직계자식
print(e)
for aa in e:
    print(aa.string)