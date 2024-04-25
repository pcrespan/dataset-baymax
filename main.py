import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# reading data
train_data = pd.read_csv("dataset/Training.csv")
test_data = pd.read_csv("dataset/Testing.csv")

print(train_data.drop(train_data.columns[len(train_data.columns)-1], axis=1))

# features (X) and target (Y)
x_train = train_data.drop("prognosis", axis=1) # selects all columns but prognosis
y_train = train_data["prognosis"]

x_test = test_data.drop("prognosis", axis=1)
y_test = test_data["prognosis"]

# training model
model =  DecisionTreeClassifier(random_state=42)
model.fit(x_test, y_test)

# prediction
y_prediction = model.predict(x_test)
print(y_prediction)
print(accuracy_score(y_test, y_prediction))