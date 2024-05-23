from src.Utils.ReadDatasets import getTestingData, getTrainingData
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

def useSVC(test_values):
    x_train, y_train = getTrainingData();    
    x_test, y_test = getTestingData();    

    # training model
    model = SVC()
    model.fit(x_train, y_train)

    y_test_prediction = model.predict(x_test)

    score = accuracy_score(y_test, y_test_prediction)

    # model predict
    prediction = model.predict(test_values)

    return [prediction[0], round(score * 100, 2)]