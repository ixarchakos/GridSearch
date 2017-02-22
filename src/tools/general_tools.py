import random
from sklearn import metrics
from sklearn.metrics import precision_recall_curve


def calculate_metrics(y_test, predicted, score_function):
    print "-" * 40
    print '\tAccuracy: ', metrics.accuracy_score(y_test, predicted)
    print '\tPrecision: ' + str(metrics.precision_score(y_test, predicted, average=None)[0])
    print '\tRecall: ' + str(metrics.recall_score(y_test, predicted, average=None)[0])
    print '\tF1: ' + str(metrics.f1_score(y_test, predicted, average=None)[0])
    cm = metrics.confusion_matrix(y_test, predicted)
    print '\t========================'
    print '\tTP: {0}\t FN: {1}\n\tTN: {2} \tFP: {3}\t'.format(cm[1][1], cm[1][0], cm[0][0], cm[0][1])
    print "-" * 40
    score(y_test, predicted, score_function)


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


def score(y_test, predicted_labels, score_function):
    print precision_recall_curve(y_test, predicted_labels)
    exit()
