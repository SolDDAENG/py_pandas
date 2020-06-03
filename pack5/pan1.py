# 교차 테이블 작성 : 행과 열로 구성되는 교차표. 변수들 간의 유의미한 차이 파악이 용이하다.
import pandas as pd

ytrue = pd.Series([2, 0, 2, 2, 0, 1, 1, 2, 0])  # 실제값
ypred = pd.Series([2, 1, 1, 2, 0, 1, 0, 1, 0])  # 예측값

kbs = pd.crosstab(ytrue, ypred, rownames=['True'], colnames=['Pred'], margins=True)
print(kbs)
print('예측 정확도 : ', (2 + 1 + 2) / 9)   # 예측 정확도 : 0.5555555555555556 -> 56%(반올림)

print('---------------------------')
des = pd.read_csv('../testdata/descriptive.csv')
print(des.info())
print(des.head(3))

data = des[['resident', 'gender', 'level', 'pass']]
print(data[:3], type(data))

table = pd.crosstab(data.resident, data.gender)
print(table)

print()
table2 = pd.crosstab([data.resident, data.gender], data.level)  # [resudent, gender]별 레벨
print(table2)