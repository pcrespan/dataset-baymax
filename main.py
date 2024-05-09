from src.DecisionTreeModel import useDecisionTree
import random
import numpy as np

# these variables needs to be changed for symptons collected from frontend and passed it to backend, then use them here
num_features = 132

test_input = []

# random list for predicting
for i in range(num_features):
    min_value = 0
    max_value = 1
    random_value = random.uniform(min_value, max_value)
    test_input.append(random_value)

dtResult = useDecisionTree(np.array(test_input).reshape(1, -1));

print(f"The current prognosis is '{dtResult[0]}' with model accuracy score {dtResult[1]}%");