from src.DecisionTreeModel import useDecisionTree
from src.RandomForestModel import useRandomForest
from src.KNeighborsModel import useKNeighbors
from src.SVCModel import useSVC
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

test_values = np.array(test_input).reshape(1, -1);

dtResult = useDecisionTree(test_values);
rfResult = useRandomForest(test_values);
knResult = useKNeighbors(test_values);
svcResult = useSVC(test_values);

print(f"DecisionTree result: '{dtResult[0]}' ({dtResult[1]}% of accuracy)");
print(f"RandomForest result: '{rfResult[0]}' ({rfResult[1]}% of accuracy)");
print(f"K-nearest result: '{knResult[0]}' ({knResult[1]}% of accuracy)");
print(f"SVC result: '{svcResult[0]}' ({svcResult[1]}% of accuracy)");