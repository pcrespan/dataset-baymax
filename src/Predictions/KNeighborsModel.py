from src.Utils.ReadDatasets import getTestingData, getTrainingData
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

def useKNeighbors(test_values):
    x_train, y_train = getTrainingData();    
    x_test, y_test = getTestingData();    

    # training model
    model = KNeighborsClassifier()
    model.fit(x_train, y_train)

    y_test_prediction = model.predict(x_test)

    score = accuracy_score(y_test, y_test_prediction)

    # model predict
    prediction = model.predict(test_values)

    return [prediction[0], round(score * 100, 2)]