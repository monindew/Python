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


from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
scaler.fit(X)
X_scaled = scaler.transform(X)

from sklearn.model_selection import GridSearchCV

svm_classifier = svm.SVC(kernel='rbf')
parameters = {'C': [0.001, 0.01, 0.1, 1, 10, 20, 100, 10000], 
              'gamma':[0.001, 0.01, 0.1, 1, 10, 20, 100, 10000]}

grid_svm = GridSearchCV(svm_classifier, param_grid= parameters, cv=5)

grid_svm.fit(X_scaled, y)
result = pd.DataFrame(grid_svm.cv_results_['params'])
result['mean_test_score'] = grid_svm.cv_results_['mean_test_score']
print(result.sort_values(by='mean_test_score', ascending=False))



# svm_classifier = svm.SVC(kernel='linear')
# result = svm_classifier.fit(X,y)
# # print(result.predict(X))
# result = cross_val_score(svm_classifier, X_scaled, y, cv=5)
# print(result)
