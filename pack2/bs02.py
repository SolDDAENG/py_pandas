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


