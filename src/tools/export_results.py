from os import path, makedirs, getcwd
from time import strftime


def write_to_file(best_model_dict, cut_off_boundary):
    filename = get_file_path('results', 'grid_search{0}.txt'.format(strftime('_%Y-%m-%d_%H.%M.%S')))
    with open(filename, 'w') as w:
        index = 1
        for k, v in best_model_dict.iteritems():
            w.write('Model with rank: {0} \n'.format(index))
            w.write('Scores according to selected criterion: {0} \n'.format(str(v[0])))
            w.write('With parameters: {0} \n'.format(v[1].get_params()))
            w.write('And cut off boundary: {0} \n'.format(cut_off_boundary))
            w.write('\n------ Classification Report ------ \n')
            stability_dict = v[1].calculate_model_stability()
            w.write('Score function - Max Value: {0} \n'.format(stability_dict["max_value"]))
            w.write('Score function - Min Value: {0} \n'.format(stability_dict["min_value"]))
            w.write('Score function - 1st quartile: {0} \n'.format(stability_dict["first_quartile"]))
            w.write('Score function - 2nd quartile: {0} \n'.format(stability_dict["second_quartile"]))
            w.write('Score function - 3rd quartile: {0} \n'.format(stability_dict["third_quartile"]))
            for key, value in v[1].calculate_averages_per_metric().iteritems():
                w.write('Metric {0} - Value: {1} \n'.format(key, str(value)))
            w.write('------ End of Classification Report ------\n\n')
            w.write(('-' * 50) + '\n')
            index += 1


def get_file_path(path_from_module, file_name):
    """
    We use this method to find the files that in many cases we need but are not visible.
    :param path_from_module: The path from the central repo to the folder we want.
    :param file_name: The file we want from the folder.
    :return: The actual path to file
    """
    if not path.exists('results'):
        makedirs('results')

    fn = path.realpath(path.join(getcwd(), path.dirname(__file__))).split("/src/")[0]
    return "{0}/{1}/{2}".format(fn, path_from_module, file_name)
