# 행열 이동, 중복 제거, 구간 단위 설정
import pandas as pd
import numpy as np

df = pd.DataFrame(1000 + np.arange(6).reshape(2, 3), index=['대전', '서울'], columns=['2017', '2018', '2019'])
print(df)
df_row = df.stack()  # 열 인덱스 -> 행 인덱스로 변환
print(df_row)
df_col = df_row.unstack()  # 행 인덱스 -> 열 인덱스로 변환
print(df_col)

print()
data = {'data1': ['a'] * 4, 'data2': [1, 1, 2, 2]}  # dict type
print(data)
df2 = pd.DataFrame(data)
print(df2)
result = df2.drop_duplicates()  # 중복 제거
print(result)

# 연속 데이터 범주화
print()
price = [10.3, 5.5, 7.8, 3.6, 5, 9]
cut = [3, 7, 9, 11]  # 구간 기준값
result_cut = pd.cut(price, cut)
print(result_cut)  # (a, b] --> a < x <= b
print(pd.value_counts(result_cut))  # 범주(범위)의 개수

print()
datas = pd.Series(np.arange(1, 1001))
print(datas)
print()
result_cut2 = pd.qcut(datas, 3)  # 구간을 개수(3)으로 나눔
print(result_cut2)  # [(0.999, 334.0] < (334.0, 667.0] < (667.0, 1000.0]]
print(pd.value_counts(result_cut2))

print('-------------------')
# merge : 명령을 사용한 데이터프레임 병합
print('--공통 칼럼이 있는 경우----')
df1 = pd.DataFrame({'data1': range(7), 'key': ['b', 'b', 'a', 'c', 'a', 'a', 'b']})
df2 = pd.DataFrame({'key': ['a', 'b', 'd'], 'data2': range(3)})
print(df1)
print(df2)
print()
print(pd.merge(df1, df2, on='key'))  # default : on = 'key' # df1과 df2 겹치는 key의 순서 출력.
print(pd.merge(df1, df2, on='key', how='inner'))  # sql의 inner join과 같다.
print()
print(pd.merge(df1, df2, on='key', how='outer'))  # sql의 full outer join
print()
print(pd.merge(df1, df2, on='key', how='left'))  # 왼쪽(첫번째) 데이터 프레임의 키 값을 모두 보여준다.
print()
print(pd.merge(df1, df2, on='key', how='right'))  # 오른쪽(두번째) 데이터프레임의 키 값을 모두 보여준다.

print('\n--공통 칼럼이 없는 경우(자료의 성격은 동일해야함)----')
df3 = pd.DataFrame({'key2': ['a', 'b', 'd'], 'data2': range(3)})
# print(pd.merge(df1, df3))     # 공통 칼럼이 없기 때문에 에러  # df1 : key1, df3 : key2
print(pd.merge(df1, df3, left_on='key', right_on='key2'))

print()
print(pd.concat([df1, df2], axis=0))    # 열 단위
print(pd.concat([df1, df2], axis=1))    # 행 단위

print('\n--np의 array 자료 이어붙이기')
arr1 = np.arange(6).reshape(2, 3)
arr2 = np.arange(4, 10).reshape(2, 3)
print(arr1)
print(arr2)
print()
arrs1 = np.concatenate([arr1, arr2], axis=0)
print(arrs1)
print()
arrs2 = np.concatenate([arr1, arr2], axis=1)
print(arrs2)