from src.Utils.ReadDatasets import getTestingData, getTrainingData
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def useRandomForest(test_values):
    x_train, y_train = getTrainingData();    
    x_test, y_test = getTestingData();    

    # training model
    model = RandomForestClassifier()
    model.fit(x_train, y_train)

    y_test_prediction = model.predict(x_test)

    score = accuracy_score(y_test, y_test_prediction)

    print("Acc score: {:.2f}%".format(score * 100))

    # model predict
    prediction = model.predict(test_values)

    return [prediction[0], round(score * 100, 2)]