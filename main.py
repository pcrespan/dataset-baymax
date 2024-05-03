import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# reading data
train_data = pd.read_csv("dataset/Training.csv")
test_data = pd.read_csv("dataset/Testing.csv")

# needs to be dropped last column created by an ',' at the end - dataset formatting
train_data = train_data.drop(train_data.columns[len(train_data.columns)-1], axis=1)

# features => symptons (0 or 1)
# target => prognosis

# features (X) and target (Y) for TRAINING
x_train = train_data.drop("prognosis", axis=1)
y_train = train_data["prognosis"]

# features (X) and target (Y) for TESTING SCORE
x_test = test_data.drop("prognosis", axis=1)
y_test = test_data["prognosis"]

# training model
model =  DecisionTreeClassifier(random_state=42)
model.fit(x_train, y_train)

y_test_prediction = model.predict(x_test)

# Testing model prediction score
score = accuracy_score(y_test, y_test_prediction)

# Some random values and suppose to return Fungal Infection as result
x_for_testing = [[1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

model.fit(x_train.values, y_train)
y_prediction = model.predict(x_for_testing)

print(f"The current prognosis is '{y_prediction[0]}' with model accuracy score {round(score * 100, 4)}%")
