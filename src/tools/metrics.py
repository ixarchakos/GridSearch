from sklearn import metrics
from sklearn.metrics import precision_recall_curve


def calculate_metrics(y_test, predicted, score_function):
    print "-" * 40
    # print '\tAccuracy: ', metrics.accuracy_score(y_test, predicted)
    print '\tPrecision: ' + str(metrics.precision_score(y_test, predicted, average=None)[0])
    print '\tRecall: ' + str(metrics.recall_score(y_test, predicted, average=None)[0])
    # print '\tF1: ' + str(metrics.f1_score(y_test, predicted, average=None)[0])
    # cm = metrics.confusion_matrix(y_test, predicted)
    # print '\t========================'
    # print '\tTP: {0}\t FN: {1}\n\tTN: {2} \tFP: {3}\t'.format(cm[1][1], cm[1][0], cm[0][0], cm[0][1])
    print "-" * 40
    return {
        'score': metrics.precision_score(y_test, predicted, average=None)[0],
        'recall': metrics.recall_score(y_test, predicted, average=None)[0]
        }
    # score(y_test, predicted, score_function)


def score(y_test, predicted_labels, score_function):
    print precision_recall_curve(y_test, predicted_labels)
    exit()
