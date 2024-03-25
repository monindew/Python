import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import sklearn.svm as svm


from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split

df = pd.read_csv('train.csv')

#데이터 형식 변경

df['HighPrice'] = (df['SalePrice'] >= 100000).astype(int)

X = df[['LotArea', 'OverallQual', 'OverallCond', 'YearBuilt']]
y = df['HighPrice']



x_train, x_test, y_train, y_test = train_test_split(X, y, 
                                                    stratify=y, random_state=0)
gbc = GradientBoostingClassifier( random_state=0, max_depth=2, learning_rate=0.05) # 기본값: max_depth=3, learning_rate=0.1
gbc.fit(x_train, y_train)
print(gbc.score(x_train, y_train))
print(gbc.score(x_test, y_test))