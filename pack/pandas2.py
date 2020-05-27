# pandas 기능
from pandas import Series, DataFrame

# 재색인----------
data = Series([1, 2, 3], index=(1, 4, 2))
print(data)

data2 = data.reindex((1, 2, 4))
print(data2)

# 재색인하며 값 채우기
data3 = data2.reindex((1, 2, 3, 4, 5))
print(data3)

print()
data3 = data2.reindex([1, 2, 3, 4, 5], fill_value=777)  # fill_value=777 : NaN값을 777로 채움
print(data3)

print('---채움1---')
data3 = data2.reindex([1, 2, 3, 4, 5], method='ffill')  # ffill : 채우는 값이 그 이전 값을 가져옴. # 엑셀의 Ctrl + D 같은 느낌
print(data3)
data3 = data2.reindex([1, 2, 3, 4, 5], method='pad')  # pad : 위와 같다
print(data3)

print('---채움2---')
data3 = data2.reindex([1, 2, 3, 4, 5], method='bfill')
print(data3)
data3 = data2.reindex([1, 2, 3, 4, 5], method='backfill')  # NaN을 그 다음 값이 (아래 있는 값이) 채움. 위 채움1과 반대
print(data3)

print('^^^' * 10)
import numpy as np

df = DataFrame(np.arange(12).reshape(4, 3), index=['1월', '2월', '3월', '4월'],
               columns=['강남', '강북', '서초'])
print(df)
print(df['강남'])
print(df['강남'] > 3)
print(df[df['강남'] > 3])  # (df['강남'] > 3) 에서 True인 행만 출력

print()
print(df < 3)
df[df < 3] = 0
print(df)

print('DataFrame 슬라이싱 관련 메소드')
# loc : 라벨 지원(라벨만 쓸 수 있다), iloc : 숫자 지원
print('loc')
print(df.loc['3월',])
print(df.loc['3월', :])  # 3월의 모든 열

print(df.loc[:'2월'])
print(df.loc[:'2월', ['서초']])
print(df.loc[:'2월', ['서초', '강남']])

print('\niloc')
print(df.iloc[2])
print(df.iloc[2, :])  # 2행의 모든 열
print(df.iloc[:3, 2])
print(df.iloc[:3, 1:3])  # 1열 부터 3열 미만

print('\n\n산술연산------------')
s1 = Series([1, 2, 3], index=['a', 'b', 'c'])
s2 = Series([4, 5, 6, 7], index=['a', 'b', 'd', 'c'])
print(s1)
print(s2)
print(s1 + s2)
print(s1.add(s2))  # 같은 인덱스명이 대응될 때 연산 가능(인덱스가 같아야 한다)

print()
df1 = DataFrame(np.arange(9.).reshape(3, 3), columns=list('kbs'), index=['서울', '인천', '수원'])
print(df1)
df2 = DataFrame(np.arange(12.).reshape(4, 3), columns=list('kbs'), index=['서울', '인천', '일산', '수원'])
print(df2)

print()
print(df1 + df2)  # 얘는 속성을 쓸 수 없다.
print(df1.add(df2))  # 얘는 속성을 쓸 수 있다.
print(df1.add(df2, fill_value=0))   # 얘는 속성(ex. fill_value)를 쓸 수 있다.

print()
print(df1 + df2)
print(df1.mul(df2)) # mul : 곱하기
print(df1.mul(df2, fill_value=0))

print()
seri = df1.iloc[0]  # df1의 1열 모두 출력
print(seri)
print(df1 - seri)   # broadcasting되서 연산 가능