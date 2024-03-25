import pandas as pd
# 딕셔너리
data = {
    'apples' : [3, 2, 1, 5],
    'oranges': [2, 4, 1, 7]
}
df = pd.DataFrame(data, index = ['바구니1', '바구니2', '바구니3', '바구니4']) 
print(df)

df = pd.read_csv('grade.csv', index_col=0)
print(df)

print(df.info())