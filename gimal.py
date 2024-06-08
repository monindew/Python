import pandas as pd
from sklearn.model_selection import train_test_split
<<<<<<< HEAD
from sklearn.preprocessing import MinMaxScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import confusion_matrix, classification_report, roc_curve, auc
import matplotlib.pyplot as plt

dividend_data = pd.read_csv("dividend.csv")

X = dividend_data.iloc[:, 1:6]
y = dividend_data['dividend']

scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.25, random_state=123)

nn_model = MLPClassifier(hidden_layer_sizes=(1,), max_iter=1000, random_state=123)
nn_model.fit(X_train, y_train)
nn_pred = nn_model.predict(X_test)
nn_pred_prob = nn_model.predict_proba(X_test)[:, 1]

conf_matrix = confusion_matrix(y_test, nn_pred)
class_report = classification_report(y_test, nn_pred)

print("Confusion Matrix:\n", conf_matrix)
print("\nClassification Report:\n", class_report)

fpr, tpr, _ = roc_curve(y_test, nn_pred_prob)
roc_auc = auc(fpr, tpr)

plt.figure()
plt.plot(fpr, tpr, color='darkorange', lw=2, label='ROC curve (area = %0.2f)' % roc_auc)
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic')
plt.legend(loc="lower right")
plt.show()
=======
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
>>>>>>> a43ea66b2d2c3afbc095a70b6b627207ccfe49c8
