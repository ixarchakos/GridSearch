from src.model.GridSearch import GridSearch
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier


param_grid = {"n_estimators": [i for i in range(200, 601, 50)],
              "max_features": [i for i in range(8, 13, 1)],
              "criterion": ["gini", "entropy"]
              }

iris = datasets.load_iris()
x = iris.data[:, :2]
y = iris.target

grid = GridSearch(RandomForestClassifier(), param_grid, 1, 1, 5)
print grid.fit(x, y, [i / 100.0 for i in range(60, 80, 1)])
