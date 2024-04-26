import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# reading data
train_data = pd.read_csv("dataset/Training.csv")
test_data = pd.read_csv("dataset/Testing.csv")

# needs to be dropped last column created by an ',' at the end
train_data = train_data.drop(train_data.columns[len(train_data.columns)-1], axis=1)
dataset_headers = train_data.head(0)


# features => symptons
# target => prognosis

# features (X) and target (Y)
x_train = train_data.drop("prognosis", axis=1) # selects all columns but not prognosis
y_train = train_data["prognosis"]

# x_test = test_data.drop("prognosis", axis=1)
# y_test = test_data["prognosis"]

# training model
model =  DecisionTreeClassifier(random_state=42)
model.fit(x_train.values, y_train)
# it's supposed to return Fungal Infection as response
x_for_testing = [[1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

# prediction
y_prediction = model.predict(x_for_testing)
print(y_prediction)