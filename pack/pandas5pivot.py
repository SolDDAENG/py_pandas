# 그룹화, 피벗...
import numpy as np
import pandas as pd

data = {'city': ['강남', '강북', '강남', '강북'],
        'year': [2010, 2011, 2012, 2012],
        'pop': [3.3, 2.5, 3.0, 2.0]}
df = pd.DataFrame(data)
print(df)

# 행/열 별 연산
print(df.pivot('city', 'year', 'pop'))  # 행, 열 연산칼럼
print(df.pivot('year', 'city', 'pop'))
print()
print(df.set_index(['city', 'year']).unstack())
print(df.set_index(['year', 'city']).unstack())

print()
hap = df.groupby(['city'])
print(hap.sum())
print(df.groupby(['city']).sum())
print(df.groupby(['city', 'year']).mean())

print('-------------')
print(df)
print(df.pivot_table(index=['city']))  # pop과 year에 대한 평균
# 중요한것 : value, aggfunc         # aggfunc 뒤에는 함수의 이름만 줘야함. mean : O, mean() : X
print(df.pivot_table(index=['city'], aggfunc=np.mean))  # default : mean   # mean : O, mean() : X   # 위와 같음
print(df.pivot_table(index=['city', 'year'], aggfunc=np.mean))
print(df.pivot_table(index=['city', 'year'], aggfunc=[len, np.mean]))  # len : 도시의 각 연도별 pop의 개수
print()
print(df.pivot_table(values=['pop'], index=['city']))  # pop의 city별 평균
print(df.pivot_table(['pop'], index=['city']))  # values는 안써도 괜찮..  # default : mean
print(df.pivot_table(['pop'], index='city', aggfunc=len))  # city별 pop의 개수
print()
print(df.pivot_table(['pop'], index=['year'], columns=['city']))
print(df.pivot_table(['pop'], index=['year'], columns=['city'],
                     margins=True))  # margins : 모든 데이터를 분석한 결과를 오른쪽과 아래에 붙일지 여부
print(
    df.pivot_table(['pop'], index=['year'], columns=['city'], margins=True, fill_value=0))  # fill_value=0 : NaN을 0으로 채움
