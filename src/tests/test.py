from src.model.GridSearch import GridSearch
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
import pandas as pd

param_grid = {
              "n_estimators": [i for i in range(200, 601, 50)],
              "max_features": [i for i in range(1, 3, 1)],
              "criterion": ["gini", "entropy"]
              }
df = pd.read_csv('feature_matrix_train.csv', sep=',', header=False)
df.__delitem__('job_id')
x = df.values[:, :-1]
y = df.values[:, -1]

grid = GridSearch(RandomForestClassifier(), param_grid, 'pr_auc', 1, 5)
print grid.fit(x, y, [i / 100.0 for i in range(60, 80, 1)])
