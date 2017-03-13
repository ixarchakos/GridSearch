from numpy import median, percentile


def max_value(lst):
    return max(lst)


def min_value(lst):
    return min(lst)


def mean_value(lst):
    return float(reduce(lambda x, y: x + y, lst)) / float(len(l))


def median_value(lst):
    return median(lst)


def first_quartile(lst):
    print percentile(lst, 25)


def second_quartile(lst):
    print percentile(lst, 50)


def third_quartile(lst):
    print percentile(lst, 75)
