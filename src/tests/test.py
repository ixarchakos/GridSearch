from src.model.GridSearch import GridSearch
from sklearn.ensemble import RandomForestClassifier
import pandas as pd


param_grid = {
              "n_estimators": [i for i in range(200, 601, 250)],
              "max_features": [i for i in range(2, 3, 1)],
              "criterion": ["gini", "entropy"],
              "n_jobs": [3]
              }
threshold = [i / 100.0 for i in range(78, 80, 1)]

df = pd.read_csv('feature_matrix_train.csv', sep=',', header=0)
df.__delitem__('job_id')
x = df.values[:4000, :-1]
y = df.values[:4000, -1]

grid = GridSearch(RandomForestClassifier(), param_grid, 'f1', n_times=1, k_folds=2, n_top=6, shuffle=True)
grid.fit(x, y, threshold)
