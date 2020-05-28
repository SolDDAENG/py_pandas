# file로 저장
import pandas as pd

items = {'apple': {'count': 10, 'price': 1500}, 'orange': {'count': 5, 'price': 1000}}
df = pd.DataFrame(items)
print(df)

# df.to_csv('result1.csv', sep=',')   # 현재 폴더에 ,로 구분된 csv저장
# df.to_csv('result2.csv', sep=',', index=False)  # 색인 제외
# df.to_csv('result3.csv', sep=',', index=False, header=False)    # 색인 제외, 헤더 제외
print('\n', df)
data = df.T  # DataFrame 에서 index 와 column 을 바꾼 형태의 DataFrame
print(data)
print()
df.to_csv('result4.csv', sep=',', index=False, header=True)
redata = pd.read_csv('result4.csv')
print(redata)

print('\n---exel---------')
df2 = pd.DataFrame({'data': [1, 2, 3, 4, 5]})
print(df2)
# writer = pd.ExcelWriter('good.xlsx', engine='xlsxwriter')
# df2.to_excel(writer, sheet_name='Sheet1')
# writer.save()
# print('저장 성공')

exf = pd.ExcelFile('good.xlsx')
print(exf.sheet_names)
df3 = exf.parse("Sheet1")   # parse : xlsx을 데이터프레임 값으로 바꿔줌.
print(df3)

print()
# df4 = pd.read_excel(open('good.xlsx', 'rb'))    # rb : read binary
df4 = pd.read_excel(open('good.xlsx', 'rb'), sheet_name='Sheet1')
print(df4)