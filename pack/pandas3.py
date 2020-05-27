# pandas : 기술적 통계와 관련됨 함수, NaN
from pandas import Series, DataFrame
import numpy as np

df = DataFrame([[1.4, np.nan], [7, -4.5], [np.NaN, np.NAN], [0.5, -1]], columns=['one', 'two'])
print(df)
print(df.drop(1))  # 1행을 삭제
print(df.dropna())  # NaN이 단 하나라도 있으면 삭제
print(df.dropna(how='any'))  # NaN이 단 하나라도 있으면 삭제
print(df.dropna(how='all'))  # NaN으로 전부 차 있는 행만 제거한다 - 하나만 NaN이면 삭제하지 않음.
print(df.dropna(subset=['one']))  # 칼럼명이 one인 곳에서 NaN이 있는 행을 지움
print(df.fillna(0))  # NaN을 fillna( )의 값으로 채우기. sklearn 모듈의 SimpleInputer

# 기술적 통계와 관련된 함수
print('**' * 10)
print(df.sum())
print(df.sum(axis=0))  # 열의 합
print()
print(df.sum(axis=1))  # 행의 합
print(df.mean(axis=1))  # 행의 평균
print(df.sum(axis=1, skipna=True))  # skipna=True : NaN이 있어도 계산.
print(df.sum(axis=1, skipna=False))  # skipna=False : NaN이 있는 행은 NaN으로 출력

print()
print(df.max())
print(df.max(axis=0))
print(df.max(axis=1))
print(df.idxmax())  # index를 반환
print(df.idxmin())

print()
print(df.describe())  # 요약 통계량
print()
print(df.info())  # 구조
print()
words = Series(['봄', '여름'])
print(words.describe())
# print(words.info())  # Series엔 info가 없다.   # AttributeError: 'Series' object has no attribute 'info'
