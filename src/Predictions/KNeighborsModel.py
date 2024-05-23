from src.Utils.ReadDatasets import getTestingData, getTrainingData
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler

def useKNeighbors(test_values):
    x_train, y_train = getTrainingData();    
    x_test, y_test = getTestingData();    

    scaler = StandardScaler()
    x_train = scaler.fit_transform(x_train)
    x_test = scaler.transform(x_test)

    model = KNeighborsClassifier(n_neighbors=3)
    model.fit(x_train, y_train)


    y_test_prediction = model.predict(x_test)

    score = accuracy_score(y_test, y_test_prediction)
    
    prediction = model.predict(scaler.transform(test_values))

    return [prediction[0], round(score * 100, 2)]