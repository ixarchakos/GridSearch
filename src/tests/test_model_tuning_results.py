from src.model.ModelTuningResults import ModelTuningResults

param_grid = {
              "n_estimators": [i for i in range(200, 601, 50)],
              "max_features": [i for i in range(1, 3, 1)],
              "criterion": ["gini", "entropy"]
              }

people = {'name': "Tom", 'score': 10}

people1 = {'name': "Tom", 'score': 3}

c = ModelTuningResults(param_grid)
c.add_results(people)
c.add_results(people1)
print c.calculate_model_score()
