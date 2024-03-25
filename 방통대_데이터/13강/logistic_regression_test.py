import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm

df = pd.read_csv('train.csv')

#데이터 형식 변경

df['HighPrice'] = (df['SalePrice'] >= 100000).astype(int)

# 결과 확인
print(df.head())
print(df['HighPrice'].sum() / df['HighPrice'].count())

#x,y 선택
X = df[['LotArea', 'OverallQual', 'OverallCond', 'YearBuilt']]
y = df['HighPrice']
X = sm.add_constant(X)

# from sklearn.feature_selection import chi2, SelectKBest
# selector1 = SelectKBest(chi2, k=3)
# X = selector1.fit_transform(X, y)
# print(X)

logit = sm.Logit(y, X)
result = logit.fit()
print(result.summary())
print(result.params)

# boundary = 1980
# sns.scatterplot(x = 'YearBuilt', y = 'HighPrice', data = df).set(xlim=(1900,2100))
# plt.plot([boundary, boundary], [0, 1], 'g', linewidth = 6)

# plt.show()

y_pred = result.predict(X)
sns.scatterplot(x = df['OverallQual'], y = y_pred, hue = df['HighPrice']).set(xlim=(0,10))
plt.show()