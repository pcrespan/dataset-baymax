import pandas as pd

# features (X) => symptons 
# target (Y) => prognosis
def getTrainingData():
    train_data = pd.read_csv("dataset/Training.csv")
    
    missing_values = train_data.isnull()
    missing_count = missing_values.sum()
    
    print("Missing values per column (Training):")
    print(missing_count)

    # remove last column from training.csv because it's null
    train_data.drop(columns=['Unnamed: 133'], inplace=True)
    
    x_train = train_data.drop(columns=["prognosis"])
    y_train = train_data["prognosis"]

    return [x_train, y_train]

def getTestingData():
    test_data = pd.read_csv("dataset/Testing.csv")

    missing_values = test_data.isnull()

    missing_count = missing_values.sum()

    print("Missing values per column:")
    print(missing_count)

    x_test = test_data.drop(columns=["prognosis"])
    y_test = test_data["prognosis"]

    return [x_test, y_test]