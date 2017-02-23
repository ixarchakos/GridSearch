class ModelTuningResults:

    def __init__(self, model_id, parameters, threshold, n_times, n_folds):
        self.model_id = model_id
        self.parameters = parameters
        self.threshold = threshold
        self.n_times = n_times
        self.n_folds = n_folds
        self.result_list = list()

    def add_results(self, results):
        self.result_list.append(results)

    def calculate_model_score(self):
        final_score = 0
        for dict_scores in self.result_list:
            final_score += dict_scores["score"]
        return float(final_score) / float(self.result_list.__len__())

    def get_model_id(self):
        return self.model_id

    def get_params(self):
        return self.parameters
