from src.Utils.ReadDatasets import getTestingData, getTrainingData
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

def useDecisionTree(test_values):
    x_train, y_train = getTrainingData();    
    x_test, y_test = getTestingData();    

    # training model
    model = DecisionTreeClassifier(random_state=42)
    model.fit(x_train, y_train)

    y_test_prediction = model.predict(x_test)

    score = accuracy_score(y_test, y_test_prediction)

    print("Acc score: {:.2f}%".format(score * 100))

    # model predict
    prediction = model.predict(test_values)

    return [prediction[0], round(score * 100, 2)]