from numpy import median, percentile


def max_value(lst):
    """
    Calculates the max value of a given list
    :param lst: list
        - A python list
    :return: float
        - The max value
    """
    return max(lst)


def min_value(lst):
    """
    Calculates the min value of a given list
    :param lst: list
        - A python list
    :return: float
        - The min value
    """
    return min(lst)


def mean_value(lst):
    """
    Calculates the mean value of a given list
    :param lst: list
        - A python list
    :return: float
        - The mean value
    """
    return float(reduce(lambda x, y: x + y, lst)) / float(len(lst))


def median_value(lst):
    """
    Calculates the median value of a given list
    :param lst: list
        - A python list
    :return: float
        - The median value
    """
    return median(lst)


def first_quartile(lst):
    """
    Calculates the first quartile of a given list
    :param lst: list
        - A python list
    :return: float
        - The first quartile
    """
    return percentile(lst, 25)


def second_quartile(lst):
    """
    Calculates the second quartile of a given list
    :param lst: list
        - A python list
    :return: float
        - The second quartile
    """
    return percentile(lst, 50)


def third_quartile(lst):
    """
    Calculates the third quartile of a given list
    :param lst: list
        - A python list
    :return: float
        - The third quartile
    """
    return percentile(lst, 75)
