import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score

data = pd.read_csv('bank-market.csv')

selected_vars = ["age", "job", "marital", "education", "default", "balance", "housing", "loan", "y"]
data = data[selected_vars]

categorical_vars = ["job", "marital", "education", "default", "housing", "loan", "y"]
for var in categorical_vars:
    data[var] = data[var].astype('category').cat.codes

train_data, test_data = train_test_split(data, test_size=0.25, random_state=123)

X_train = train_data.drop('y', axis=1)
y_train = train_data['y']
X_test = test_data.drop('y', axis=1)
y_test = test_data['y']

tree_model = DecisionTreeClassifier(random_state=123)
tree_model.fit(X_train, y_train)

tree_pred = tree_model.predict(X_test)

conf_matrix = confusion_matrix(y_test, tree_pred)
accuracy = accuracy_score(y_test, tree_pred)
class_report = classification_report(y_test, tree_pred)

print("Confusion Matrix:\n", conf_matrix)
print("\nAccuracy:", accuracy)
print("\nClassification Report:\n", class_report)
