import os
import time


def write_to_file(best_model_dict, cut_off_boundary):
    filename = get_file_path('results', 'grid_search{0}.txt'.format(time.strftime('_%Y-%m-%d_%H.%M.%S')))
    with open(filename, 'w') as w:
        index = 1
        for k, v in best_model_dict.iteritems():
            w.write('Model with rank: {0} \n'.format(index))
            index += 1
            w.write('Scores according to selected criterion: {0} \n'.format(str(v[0])))
            w.write('With parameters: {0} \n'.format(v[1].get_params()))
            w.write('And cut off boundary: {0} \n'.format(cut_off_boundary))
            w.write(('*' * 30) + '\n')
            w.write('------ Classification Report ------ \n')
            # TODO
            w.write(('-' * 50) + '\n')


def get_file_path(path_from_module, file_name):
    """
    We use this method to find the files that in many cases we need but are not visible.
    :param path_from_module: The path from the central repo to the folder we want.
    :param file_name: The file we want from the folder.
    :return: The actual path to file
    """
    if not os.path.exists('results'):
        os.makedirs('results')

    fn = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__))).split("/src/")[0]
    return "{0}/{1}/{2}".format(fn, path_from_module, file_name)
