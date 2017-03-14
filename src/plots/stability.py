from pylab import show, savefig, xlim, figure, hold, ylim, boxplot, setp, axes
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
        savefig('box_plot' + str(iteration) + '.png')
    show()



