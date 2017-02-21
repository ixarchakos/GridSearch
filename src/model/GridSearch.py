import itertools
from sklearn import *


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
        key_list = list()
        values_list = list()
        for key, value_list in self.param_grid.iteritems():
            key_list.append(key)
            values_list.append(value_list)
        values_list.append(thres)
        key_list.append('threshold')
        for tuples in list(itertools.product(*values_list)):
            parameters_dict = dict()
            for i, t in enumerate(tuples):
                parameters_dict[key_list[i]] = str(t)
            cut_off_boundary = parameters_dict['threshold']
            del parameters_dict['threshold']

            for i in range(0, self.n_times, 1):
                for j in range(0, self.k_folds, 1):
                    print self.algorithm.set_params(**parameters_dict)

    @staticmethod
    def check_param_compatibility(self):
        print self.algorithm
        if False:
            print 'Incompatible grid parameters'
