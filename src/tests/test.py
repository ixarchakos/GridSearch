from src.model.GridSearch import GridSearch
from sklearn.ensemble import RandomForestClassifier
import pandas as pd

# grid parameters and threshold
param_grid = {
              "n_estimators": [i for i in range(200, 601, 250)],
              "max_features": [i for i in range(2, 3, 1)],
              "criterion": ["gini", "entropy"],
              "n_jobs": [4]
              }
threshold = [i / 100.0 for i in range(77, 80, 1)]

# import and manipulate data
df = pd.read_csv('feature_matrix_train.csv', sep=',', header=0)
df.__delitem__('job_id')
x = df.values[:4000, :-1]
y = df.values[:4000, -1]

# start of grid search
GridSearch(RandomForestClassifier(), param_grid, 'f1', n_times=6, k_folds=4, n_top=10, bootstrap=False, evaluation_class=None).fit(x, y, threshold)

