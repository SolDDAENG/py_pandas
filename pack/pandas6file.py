# file 읽기
import pandas as pd

df = pd.read_csv("../testdata/ex1.csv")
print(df, type(df))

print()
df = pd.read_table("../testdata/ex1.csv", sep=',')  # ,를 구분
print(df)

print()
df = pd.read_csv("../testdata/ex2.csv", header=None)  # header가 없는 파일. 이때 header=None을 주면 columns에 0 1 2 3 4가 찍힌다.
print(df)

print()
# df = pd.read_csv("../testdata/ex2.csv", header=None, names=['a', 'b'])  # names는 오른쪽부터 채워짐
df = pd.read_csv("../testdata/ex2.csv", header=None,
                 names=['a', 'b', 'c', 'd', 'e', 'f'])  # # names를 범위보다 더 주면 NaN으로 값이 채워진채로 늘어난다.
print(df)

print()
df = pd.read_csv("../testdata/ex2.csv", header=None, names=['a', 'b', 'c', 'd', 'e'],
                 index_col='e')  # 칼럼을 인덱스로 붙일 수 있다.
print(df)

print()
df = pd.read_table("../testdata/ex3.txt")
print(df)

print()
df = pd.read_csv("../testdata/ex3.txt")
print(df)

print()
df = pd.read_csv("../testdata/ex3.txt", sep='\s+', skiprows=[1, 3])  # skiprows = [1, 3] (1, 3)  list, tuple 둘 다 가능
print(df)

print('\n간격으로 구분하기')
df2 = pd.read_fwf("../testdata/data_fwt.txt", widths=(10, 3, 5), names=('날짜', '기업명', '가격'))
print(df2)

print()
# chunk : 대용량의 파일인 경우에는 원하는 크기만큼 할당해서 읽기
datas = pd.read_csv('../testdata/data_csv2.csv', header=None, chunksize=3)  # chunksize=3   : 3개씩 구분
print(datas)  # TextFileReader object

for p in datas:
    # print(p)
    print(p.sort_values(by=2, ascending=True))
