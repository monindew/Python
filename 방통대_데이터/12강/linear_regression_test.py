import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

 
from sklearn.linear_model import LinearRegression

df = pd.read_csv('train.csv')
df = df[['SalePrice', 'LotArea']]

# print(df.head())


model = LinearRegression()
model.fit(X=df[['LotArea']], y=df['SalePrice']) #x가 다변수일 수 있으므로 [] 한겹 추가

print("기울기 : ", model.coef_, "절편 : ", model.intercept_)

print(model.predict([[1000]]))


# ax = sns.scatterplot(df, x="SalePrice", y="LotArea")
# ax.set(ylim=(0,50000))

# plt.show()

import statsmodels.api as sm
 
x = df['LotArea']
y = df['SalePrice']
 
#add constant to predictor variables
x = sm.add_constant(x)
 
model = sm.OLS(y, x).fit()
 
print(model.summary())