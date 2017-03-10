from collections import OrderedDict
from sklearn import metrics
from warnings import filterwarnings
filterwarnings("ignore", category=DeprecationWarning)


def calculate_metrics(y_test, predicted, predicted_probabilities, score_function, evaluation_class):
    metrics_results = OrderedDict()
    metrics_results['score'] = score(y_test, predicted, score_function, predicted_probabilities, evaluation_class)
    metrics_results['accuracy'] = metrics.accuracy_score(y_test, predicted)

    # precision
    metrics_results['avg_precision'] = metrics.precision_score(y_test, predicted, average='macro')
    for i, value in enumerate(metrics.precision_score(y_test, predicted, average=None)):
        metrics_results['precision_in_class_'+str(i)] = value

    # recall
    metrics_results['avg_recall'] = metrics.recall_score(y_test, predicted, average='macro')
    for i, value in enumerate(metrics.recall_score(y_test, predicted, average=None)):
        metrics_results['recall_in_class_'+str(i)] = value

    # f1
    metrics_results['avg_f1'] = metrics.f1_score(y_test, predicted, average='macro')
    for i, value in enumerate(metrics.f1_score(y_test, predicted, average=None)):
        metrics_results['f1_in_class_'+str(i)] = value

    # log-loss
    metrics_results['log_loss'] = metrics.log_loss(y_test, predicted_probabilities)

    # confusion matrix
    cm = metrics.confusion_matrix(y_test, predicted)
    metrics_results['true_positives'] = cm[1][1]
    metrics_results['false_negatives'] = cm[1][0]
    metrics_results['true_negatives'] = cm[0][0]
    metrics_results['false_positives'] = cm[0][1]

    return metrics_results


def score(y_test, predicted, score_function, predicted_probabilities, evaluation_class):
    final_score = -1
    if score_function == 'pr_auc':
        # it is not right
        final_score = metrics.precision_recall_curve(y_test, predicted)
        print final_score
        exit()
    elif score_function == 'precision':
        if evaluation_class is None:
            final_score = metrics.precision_score(y_test, predicted, average='macro')
        else:
            final_score = metrics.precision_score(y_test, predicted, average=None)[evaluation_class]
    elif score_function == 'recall':
        if evaluation_class is None:
            final_score = metrics.recall_score(y_test, predicted, average='macro')
        else:
            final_score = metrics.recall_score(y_test, predicted, average=None)[evaluation_class]
    elif score_function == 'f1':
        if evaluation_class is None:
            final_score = metrics.f1_score(y_test, predicted, average='macro')
        else:
            final_score = metrics.f1_score(y_test, predicted, average=None)[evaluation_class]
    elif score_function == 'log_loss':
            final_score = metrics.log_loss(y_test, predicted_probabilities)

    return final_score
