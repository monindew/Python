import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
import sklearn.svm as svm

from sklearn.model_selection import cross_val_score


df = pd.read_csv('train.csv')

#데이터 형식 변경

df['HighPrice'] = (df['SalePrice'] >= 100000).astype(int)

X = df[['LotArea', 'OverallQual', 'OverallCond', 'YearBuilt']]
y = df['HighPrice']

svm_classifier = svm.SVC(kernel='linear')
# result = svm_classifier.fit(X,y)
# print(result.predict(X))

score = cross_val_score(svm_classifier, X, y, cv=5)
print(score)