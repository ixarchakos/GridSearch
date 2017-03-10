from random import shuffle
from sklearn.cross_validation import KFold


def random_sample_data_set(x, y, folds):
    # random shuffle
    data = list()
    for i, value in enumerate(x.tolist()):
        value.extend([y.tolist()[i]])
        data.append(value)
    shuffle(data)
    x_train = [item[:-1] for item in data[(x.shape[0] / folds):]]
    x_test = [item[:-1] for item in data[:(x.shape[0] / folds)]]
    y_train = [item[-1] for item in data[(x.shape[0] / folds):]]
    y_test = [item[-1] for item in data[:(x.shape[0] / folds)]]

    return x_train, y_train, x_test, y_test


def k_fold_sample_data_set(x, y, folds):
    # k-fold grid search
    x_train_list, y_train_list, x_test_list, y_test_list = list(), list(), list(), list()
    try:
        kf = KFold(x.shape[0], n_folds=folds, shuffle=True)
        for train_index, test_index in kf:
            x_train_list.append(x[train_index])
            y_train_list.append(y[train_index])
            x_test_list.append(x[test_index])
            y_test_list.append(y[test_index])
        return x_train_list, y_train_list, x_test_list, y_test_list
    except AttributeError as e:
        print (e.message, "- Please, use numpy arrays as inputs")
        exit()
