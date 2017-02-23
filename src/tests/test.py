from src.model.GridSearch import GridSearch
from sklearn.ensemble import RandomForestClassifier
import pandas as pd


param_grid = {
              "n_estimators": [i for i in range(200, 601, 150)],
              "max_features": [i for i in range(2, 3, 1)],
              "criterion": ["gini", "entropy"],
              "n_jobs": 3
              }

df = pd.read_csv('feature_matrix_train.csv', sep=',', header=0)
df.__delitem__('job_id')
x = df.values[:4000, :-1]
y = df.values[:4000, -1]

grid = GridSearch(RandomForestClassifier(), param_grid, 'pr_auc',
                  n_times=1, k_folds=3, n_top=6, shuffle=True)

print grid.fit(x, y, [i / 100.0 for i in range(78, 80, 1)])
