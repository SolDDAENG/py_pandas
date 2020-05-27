# pandas module : 고수준의 자료구조(Series, DataFrame)를 지원
from pandas import Series
import numpy as np

obj = Series([3, 7, -5, 4])  # list type
# obj = Series((3, 7, -5, 4)) # tuple type
# obj = Series({3, 7, -5, 4}) # set type은 지원 X
print(obj, type(obj))

print()
obj2 = Series([3, 7, -5, 4], index=['a', 'b', 'c', 'd'])
print(obj2, type(obj2))
print(obj2.sum(), ' ', sum(obj2), ' ', np.sum(obj2))
print(obj2.mean(), obj2.std())  # numpy에서 지원하는 함수를 pandas에서도 지원한다.  # mean : 평균, std : 표준편차
print()
print('배열값 : ', obj2.std())
print('색인 : ', obj2.index)

print('\n 슬리아싱----')
print(obj2['a'])  # 3 : 값만 나옴
print(obj2[0])  # 3 : 값만 나옴
print(obj2[['a']])  # a     3 : 색인과 값이 같이 나온다.
print(obj2[[0]])  # a     3 : 색인과 값이 같이 나온다
print()
print(obj2[['a', 'b']])
print(obj2['a':'c'])
print()
print(obj2[2])
print(obj2[2:4])
print(obj2[[2, 1]])
print(obj2 > 0)
print('a' in obj2)  # obj2에 a가 있으면 True, 없으면 False
print('k' in obj2)

print('\n--dict---------')
names = {'mouse': 5000, 'keyboard': 350000, 'monitor': 550000}  # dict type
print(names, type(names))
obj3 = Series(names)
print(obj3)
obj3.index = ['마우스', '키보드', '모니터']
print(obj3)
obj3.name = '상품가격'
print(obj3)

print('---DataFrame--------')
from pandas import DataFrame

df = DataFrame(obj3)
print(df, type(df))

print()
data = {
    'irum': ['홍길동', '신선헤', '공기밥', '한송이', '신기해'],
    'juso': ('역삼동', '신길동', '역삼동', '역심동', '서초동'),
    'nai': (23, 25, 23, 20, 26),
}
print(data, type(data))

frame = DataFrame(data)
print(frame, type(frame))
print(frame['irum'])
print(frame.irum)
print()
print(DataFrame(data, columns=['juso', 'irum', 'nai']))  # 출력의 순서를 바꿀 수 있다.
frame2 = DataFrame(data, columns=['irum', 'nai', 'juso', 'tel'], index=['a', 'b', 'c', 'd', 'e'])
print(frame2)  # tel은 결측값.(NaN : 데이터가 없다.)

print()
frame2['tel'] = '111-1111'
print(frame2)

val = Series(['222-2222', '333-3333', '444-4444'], index=['b', 'c', 'e'])
frame2['tel'] = val
print(frame2)

print(frame2.T)
print(frame2.values)
print(frame2.values[0, 2])
print(frame2.values[0:2])

print()
# frame3 = frame2.drop('d')
frame3 = frame2.drop('d', axis=0)
print(frame3)
frame4 = frame2.drop('tel', axis=1)
print(frame4)

print()
print(frame3.sort_index(axis=0, ascending=False))  # descending
print(frame3.sort_index(axis=1, ascending=True))
print(frame3.rank(axis=0))  # 사전순으로 순위를 매김

print('\n개수 카운트')
print(frame3['juso'].value_counts())

print()
data = {
    'juso':['강남구 역삼동', '중구 신당동', '강남구 대치동'],
    'inwon':[23, 25, 15]
}
frame = DataFrame(data)
print(frame)
result1 = Series([x.split()[0] for x in frame.juso])    # list를 씀 ()
result2 = Series([x.split()[1] for x in frame.juso])
print(result1)
print(result2)
print(result2.value_counts())   # 개수 출력