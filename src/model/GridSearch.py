from collections import OrderedDict
from itertools import product
from src.tools.general_tools import write_to_file
from src.tools.metrics import calculate_metrics
from src.tools.sampling import random_sample_data_set, k_fold_sample_data_set
from src.model.ModelTuningResults import ModelTuningResults
from time import time


class GridSearch:

    def __init__(self, algorithm, param_grid, score_function,
                 n_times=5, k_folds=10, n_top=50, bootstrap=True, evaluation_class=None):

        self.algorithm = algorithm
        self.param_grid = param_grid
        self.score_function = score_function
        self.n_times = n_times
        self.k_folds = k_folds
        self.bootstrap = bootstrap
        self.n_top = n_top
        self.best_model_dict = OrderedDict()
        self.evaluation_class = evaluation_class

    def fit(self, x, y, thres):
        values_list, key_list = self.parameters_to_grid(thres)
        # must be true
        unchecked = True
        # number of models
        num_of_models = len(list(product(*values_list)))
        # iterate per model
        model_id = 1
        cut_off_boundary = 0
        x_train_list, y_train_list, x_test_list, y_test_list = list(), list(), list(), list()
        for tuples in list(product(*values_list)):
            # extract model parameters and cut off boundary
            parameters_dict, cut_off_boundary = self.extract_models_parameters(tuples, key_list)
            model = ModelTuningResults(model_id, parameters_dict, cut_off_boundary, self.n_times, self.k_folds)
            model_id += 1
            # n-times
            for i in range(0, self.n_times, 1):
                if not self.bootstrap:
                    x_train_list, y_train_list, x_test_list, y_test_list = k_fold_sample_data_set(x, y, self.k_folds)
                # k-fold
                for j in range(0, self.k_folds, 1):
                    # split data set in train and test set
                    if self.bootstrap:
                        x_train, y_train, x_test, y_test = random_sample_data_set(x, y, self.k_folds)
                    else:
                        x_train = x_train_list[j]
                        y_train = y_train_list[j]
                        x_test = x_test_list[j]
                        y_test = y_test_list[j]
                    if unchecked:
                        unchecked = self.calculate_grid_time(x, y, num_of_models, parameters_dict)
                    # fit model
                    clf = self.algorithm.set_params(**parameters_dict).fit(x_train, y_train)
                    # predict
                    predicted_probabilities = clf.predict_proba(x_test)
                    predicted_labels = [0 if r[0] > cut_off_boundary else 1 for r in predicted_probabilities]
                    # calculate results
                    model.add_results(calculate_metrics(y_test, predicted_labels, predicted_probabilities,
                                                        self.score_function, self.evaluation_class))
            self.calculate_best_models(model)
        write_to_file(self.best_model_dict, cut_off_boundary)

    def calculate_best_models(self, new_model):
        self.best_model_dict[new_model.get_model_id()] = [new_model.calculate_model_score(), new_model]
        temp = sorted(self.best_model_dict.items(), key=lambda x: x[1], reverse=True)
        self.best_model_dict.clear()
        for result in temp:
            self.best_model_dict[result[0]] = result[1]
        if len(self.best_model_dict) > self.n_top:
            self.best_model_dict.popitem()

    def calculate_grid_time(self, x, y, num_of_models, parameters_dict):
        start = time()
        x_train, y_train, x_test, y_test = random_sample_data_set(x, y, self.k_folds)
        # check param compatibility with the selected model
        self.check_param_compatibility(self.algorithm, parameters_dict, x_train, y_train)
        end = time()
        print ("Number of different models: " + str(num_of_models))
        print ("The procedure needs " + str(((end - start) * num_of_models*self.n_times*self.k_folds) / 60) + " minutes")
        return False

    def parameters_to_grid(self, thres):
        values_list, key_list = list(), list()
        for key, value_list in self.param_grid.iteritems():
            key_list.append(key)
            values_list.append(value_list)
        values_list.append(thres)
        key_list.append('threshold')
        return values_list, key_list

    @staticmethod
    def extract_models_parameters(tuples, key_list):
        parameters_dict = dict()
        for i, t in enumerate(tuples):
            parameters_dict[key_list[i]] = t
        cut_off_boundary = parameters_dict['threshold']
        del parameters_dict['threshold']
        return parameters_dict, cut_off_boundary

    @staticmethod
    def check_param_compatibility(algorithm, parameters_dict, x_train, y_train):
        try:
            algorithm.set_params(**parameters_dict).fit(x_train, y_train)
        except Exception as e:
            print ("Error Message: " + e.message)
            exit()
