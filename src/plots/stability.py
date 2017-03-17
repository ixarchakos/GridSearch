from os import path, makedirs, getcwd
from pylab import show, savefig, xlim, figure, hold, ylim, boxplot, setp, axes
from time import strftime
import numpy as np


# function for setting the colors of the box plots pairs
def set_box_colors(box_plot):
    setp(box_plot['boxes'][0], color='blue')
    setp(box_plot['caps'][0], color='blue')
    setp(box_plot['caps'][1], color='blue')
    setp(box_plot['whiskers'][0], color='blue')
    setp(box_plot['whiskers'][1], color='blue')
    setp(box_plot['fliers'][0], color='blue')
    setp(box_plot['medians'][0], color='blue')


def create_box_plots(data, iteration, save_image=True):
    flatten = [val for sublist in data for val in sublist]
    iteration_value = iteration * 5
    figure("Display models' stability according to score function")
    hold(True)
    positions, labels = list(), list()
    pos = 1
    for i, box_plot_data in enumerate(data):
        labels.append(str(i+1+iteration_value) + " best model")
        positions.append(pos)
        set_box_colors(boxplot(box_plot_data, positions=[pos], widths=0.6))
        pos += 2

    # set axes limits and labels
    xlim(0, 10)
    ylim(min(flatten) - (max(flatten)-min(flatten))/20, max(flatten) + (max(flatten)-min(flatten))/20)
    axes().set_xticklabels(labels)
    axes().set_xticks(positions)
    axes().set_yticks([float(i) for i in np.arange(min(flatten), max(flatten)+(max(flatten)-min(flatten))/15, (max(flatten)-min(flatten))/15)])
    if save_image:
        box_plots = get_file_path('plots', 'box_plot_{0}_{1}.png'.format(str(iteration), strftime('_%Y-%m-%d_%H.%M.%S')))
        savefig(box_plots)
    show()


def get_file_path(path_from_module, file_name):
    """
    This method finds the files that in many cases we need but are not visible.
    :param path_from_module: The path from the central repo to the folder we want.
    :param file_name: The file we want from the folder.
    :return: The actual path to file
    """
    if not path.exists(path_from_module):
        makedirs(path_from_module)

    fn = path.realpath(path.join(getcwd(), path.dirname(__file__))).split("/src/")[0]
    return "{0}/{1}/{2}".format(fn, path_from_module, file_name)
