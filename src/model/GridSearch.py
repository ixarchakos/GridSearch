from src.tools.general_tools import calculate_metrics, random_sample_data_set
import itertools
import time


class GridSearch:

    def __init__(self, algorithm, param_grid, score_function,
                 n_times=5, k_folds=10, n_top=50, n_jobs=1, shuffle=True):

        self.algorithm = algorithm
        self.param_grid = param_grid
        self.score_function = score_function
        self.n_times = n_times
        self.k_folds = k_folds
        self.shuffle = shuffle
        self.n_jobs = n_jobs
        self.n_top = n_top

    def fit(self, x, y, thres):
        values_list, key_list = self.parameters_to_grid(thres)

        # must be true
        unchecked = False
        # iterate per model
        num_iterations = len(list(itertools.product(*values_list)))*self.n_times*self.k_folds
        for tuples in list(itertools.product(*values_list)):
            # extract model parameters and cut off boundary
            parameters_dict, cut_off_boundary = self.extract_models_parameters(tuples, key_list)

            # n-times
            for i in range(0, self.n_times, 1):
                # k-fold
                for j in range(0, self.k_folds, 1):
                    # split data set in train and test set
                    x_train, y_train, x_test, y_test = random_sample_data_set(x, y, self.k_folds)
                    if unchecked:
                        start = time.time()
                        x_train, y_train, x_test, y_test = random_sample_data_set(x, y, self.k_folds)
                        # check param compatibility with the selected model
                        self.check_param_compatibility(self.algorithm, parameters_dict, x_train, y_train)
                        end = time.time()
                        print "Number of models: " + str(num_iterations)
                        print "The procedure needs approximate " + str(((end-start)*num_iterations)/60) + " minutes"
                        unchecked = False
                    # fit model
                    clf = self.algorithm.set_params(**parameters_dict).fit(x_train, y_train)
                    print "test size " + str(len(y_test))
                    # predict
                    predicted_labels = [0 if r[0] > cut_off_boundary else 1 for r in clf.predict_proba(x_test)]
                    print "predict size " + str(len(predicted_labels))
                    # calculate results
                    calculate_metrics(y_test, predicted_labels, self.score_function)

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
