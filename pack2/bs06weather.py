import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import pandas as pd

url = "http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp"
data = urllib.request.urlopen(url).read()  # read() : 바로 읽기
# print(data.decode('utf-8'))   # 인코딩된 데이터를 디코드한다.

soup = BeautifulSoup(data, 'lxml')
# print(soup)

title = soup.find('title').string  # <title>의 value를 출력
print(title)
# CDATA 세션안의 데이터는 번역하지 않고 일반 텍스트로 인정한다. --> parsing하지 않는다.
print(soup.find('wf'))
city = soup.find_all('city')  # list형
print(city)

cityDatas = []

for c in city:
    # print(c.string)
    cityDatas.append(c.string)

df = pd.DataFrame()
df['city'] = cityDatas
# print(df.head(3))
# tmEf = soup.select_one('location > data > tmEf')    # tmEf안되면 tmef로...
tmEf = soup.select_one('location data tmEf')
tmEf = soup.select_one('location > province + city + data > tmEf')
# 형제는 +로 표현, 부모자시근 >로 표현.
# 형제는 +로 표현, 부모자식은 >로 표현.
# <location wl_ver="3">
#     <province>서울ㆍ인천ㆍ경기도</province>
#     <city>서울</city>
#     <data>
#        <mode>A02</mode>...
print(tmEf)

tempMins = soup.select('location > province + city + data > tmn')
tempDatas = []

for t in tempMins:
    # print(t.string)
    tempDatas.append(t.string)

df['temp_min'] = tempDatas
df.columns = ['지역', '최저기온']
print(df.head(3))
print(df[0:3])
print(df.tail(2))
print(df[-2:len(df)])

# 파일로 저장
df.to_csv('날씨.csv', index=False)

print('iloc, loc------------')
print(df.iloc[0], type(df.iloc[0]))  # dtype: object <class 'pandas.core.series.Series'>

print(df.iloc[0:2], type(df.iloc[0:2]))  # <class 'pandas.core.frame.DataFrame'>
print(df.iloc[0:2, :], type(df.iloc[0:2, :]))  # <class 'pandas.core.frame.DataFrame'>
print()
print(df.iloc[0:2, 0:1])
print(df.iloc[0:2, 0:2])
print()
print(df['지역'][0:2], type(df['지역'][0:2]))  # 칼럼명 지역의 0행부터 2개까지 출력
print(df['지역'][:2])  # 위와 같다.
print(df.지역[:2])  # 위와 같다.
# print(df[:])    # print(df)와 같음
# print(df)

print('----------------------')
print(df.loc[1:3])  # 1 ~ 3행 출력. 숫자대신 문자도 가능. ex) print(df.loc['a':'c'])
print(df[1:4])
print(df.loc[[1, 3]])  # 1행과 3행을 출력할 떈 복수이기 때문에 [[]]
print(df.loc[:, '지역'])  # 전체행의 지역만 출력

print()
print(df.loc[1:3, ['최저기온', '지역']])
print(df.loc[:, '지역'][1:4])

print('----------------------')
print(df.info())  # 지역, 최저기온 둘 다 object type
df = df.astype({'최저기온': 'int'})  # 최저기온을 int type으로 바꿈
print(df.info())
print(df['최저기온'].mean())
print(df['최저기온'].describe())  # 요약정리
print()
# print(df['최저기온'] >= 19)     # True, False로 출력
print(df.loc[df['최저기온'] >= 19])
print(df.loc[(df['최저기온'] >= 18) & (df['최저기온'] <= 20)])  # & : and,  | : or
print(df.loc[df['최저기온'] >= 10, ['최저기온']][0:3])  # 최저기온이 19 이상인 지역의 최저기온의 0 ~ 3행까지 출력.
print()
print(df.sort_values(['최저기온'], ascending=True))
