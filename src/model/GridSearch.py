class GridSearch:

    def __init__(self, algorithm, param_grid, score_function, n_times=5, k_folds=10, shuffle=True):
        print n_times
        self.algorithm = algorithm
        self.param_grid = param_grid
        self.score_function = score_function
        self.n_times = n_times
        self.k_folds = k_folds
        self.shuffle = shuffle

    @staticmethod
    def fit(self, x, Y, thres=0.5):
        print x

    @staticmethod
    def check_param_compatibility(self):
        print self.algorithm
        if False:
            print 'Error'
