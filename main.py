import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import random
import numpy as np

# reading data from drive
train_data = pd.read_csv("dataset/Training.csv")
test_data = pd.read_csv("dataset/Testing.csv")

# finding missing values TEST DATA
missing_values = test_data.isnull()

# counting missing values TEST DATA
missing_count = missing_values.sum()

print("Missing values per column:")
print(missing_count)

# finding missing values TRAIN DATA
missing_values = train_data.isnull()

# counting missing values TRAIN DATA
missing_count = missing_values.sum()

print("Missing values per column:")
print(missing_count)

print(train_data['Unnamed: 133'])

train_data.drop(columns=['Unnamed: 133'], inplace=True)

# features => symptons (0 or 1)
# target => prognosis

# features (X) and target (Y) for TRAINING
x_train = train_data.drop(columns=["prognosis"])
y_train = train_data["prognosis"]

# features (X) and target (Y) for TESTING SCORE
x_test = test_data.drop(columns=["prognosis"])
y_test = test_data["prognosis"]

# training model
model = DecisionTreeClassifier(random_state=42)
model.fit(x_train, y_train)

y_test_prediction = model.predict(x_test)

score = accuracy_score(y_test, y_test_prediction)

print("Acc score: {:.2f}%".format(score * 100))

# num features
num_features = x_train.shape[1]

print("Features count:", num_features)

test_input = []

# random list for predicting
for i in range(num_features):
    min_value = 0
    max_value = 1
    random_value = random.uniform(min_value, max_value)
    test_input.append(random_value)

# convert to numpy array
test_input_array = np.array(test_input).reshape(1, -1)

# model predict
prediction = model.predict(test_input_array)

print(f"The current prognosis is '{prediction[0]}' with model accuracy score {round(score * 100, 4)}%")