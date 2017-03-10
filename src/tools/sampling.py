import random


def random_sample_data_set(x, y, folds):
    # random shuffle
    data = list()
    for i, value in enumerate(x.tolist()):
        value.extend([y.tolist()[i]])
        data.append(value)
    random.shuffle(data)
    x_train = [item[:-1] for item in data[(x.shape[0] / folds):]]
    x_test = [item[:-1] for item in data[:(x.shape[0] / folds)]]
    y_train = [item[-1] for item in data[(x.shape[0] / folds):]]
    y_test = [item[-1] for item in data[:(x.shape[0] / folds)]]

    return x_train, y_train, x_test, y_test


def k_fold_sample_data_set(x, y, folds):
    # k-fold grid search
    # TODO
    print "ok"
