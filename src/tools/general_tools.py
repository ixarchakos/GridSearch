from numpy import median


def max_value(l):
    return max(l)


def min_value(l):
    return min(l)


def mean_value(l):
    return float(reduce(lambda x, y: x + y, l)) / float(len(l))


def median_value(lst):
    return median(lst)
