from collections import OrderedDict
from src.tools.general_tools import first_quartile, second_quartile, third_quartile, mean_value, min_value, max_value


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
        return float(final_score) / float(len(self.result_list))

    def get_model_id(self):
        return self.model_id

    def get_params(self):
        return self.parameters

    def calculate_averages_per_metric(self):
        keys = [dicts.keys() for dicts in self.result_list]
        total_averages_per_metric = OrderedDict()
        for key in keys[0]:
            total_average = 0
            for dict_scores in self.result_list:
                if key != "score":
                    total_average += dict_scores[key]
            if key != "score":
                total_averages_per_metric[key] = float(total_average) / float(len(self.result_list))
        return total_averages_per_metric

    def calculate_model_stability(self):
        final_score_list = list()
        index = 0
        for i in range(0, self.n_times, 1):
            final_score = 0
            for j in range(0, self.n_folds, 1):
                final_score += self.result_list[index]["score"]
                index += 1
            final_score_list.append(float(final_score)/float(self.n_folds))

        return {'first_quartile': first_quartile(final_score_list),
                'second_quartile': second_quartile(final_score_list),
                'third_quartile': third_quartile(final_score_list),
                'mean_value': mean_value(final_score_list),
                'min_value': min_value(final_score_list),
                'max_value': max_value(final_score_list)}
