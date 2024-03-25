import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import sklearn.svm as svm

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

df = pd.read_csv('train.csv')

#데이터 형식 변경

df['HighPrice'] = (df['SalePrice'] >= 150000).astype(int)

X = df[['LotArea', 'OverallQual', 'OverallCond', 'YearBuilt']]
y = df['HighPrice']

print(y.sum()/y.count())
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
scaler.fit(X)
X = scaler.transform(X)

x_train, x_test, y_train, y_test = train_test_split(X, y, 
                                                    stratify=y, random_state=0)

knnc = KNeighborsClassifier(n_neighbors=2)
knnc.fit(x_train, y_train)
print(knnc.score(x_train, y_train))
print(knnc.score(x_test, y_test))


for k in range(1,21):
    knnc = KNeighborsClassifier(n_neighbors=k, n_jobs=-1)
    knnc.fit(x_train, y_train)
    score = knnc.score(x_test, y_test)
    print('k:', k, 'accuracy:', score)