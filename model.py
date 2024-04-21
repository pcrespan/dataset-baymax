import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# reading data
train_data = pd.read_csv("dataset/training.csv")
test_data = pd.read_csv("dataset/testing.csv")

# features (X) and target (Y)
x_train = train_data.drop("prognosis", axis=1) # selects all columns but prognosis
y_train = train_data["prognosis"]

x_test = test_data.drop("prognosis", axis=1)
y_test = test_data["prognosis"]
