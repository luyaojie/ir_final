# -*- coding: utf-8 -*-
# Model Methods
import numpy as np


def find_none_zero_indexs(labels):
    """
    Find the index which labels[index] it not 0
    :param labels:
    :return:
    """
    indexs = list()
    for i in xrange(labels.shape[0]):
        if labels[i] != 0:
            indexs.append(i)
    return np.array(indexs)


def fit_and_score(train_data_x, train_data_y, test_data_x, test_data_y, classifier):
    """
    fit train_data used classifier, and score in test_data
    :param train_data_x:
    :param train_data_y:
    :param test_data_x:
    :param test_data_y:
    :param classifier:
    :return:
    """
    assert train_data_x.shape[0] == train_data_y.shape[0]
    assert test_data_x.shape[0] == test_data_y.shape[0]
    valid_train_indexs = find_none_zero_indexs(train_data_y)
    valid_test_indexs = find_none_zero_indexs(test_data_y)
    train_x, train_y = train_data_x[valid_train_indexs], train_data_y[valid_train_indexs]
    test_x, test_y = test_data_x[valid_test_indexs], test_data_y[valid_test_indexs]
    classifier.fit(train_x, train_y)
    return classifier.score(test_x, test_y)


def fit_and_score_cv(x, y, classifier, cv_num=10, random=True):
    """
    fit train_data used classifier, and score in test_data on one task
    :param x:
    :param y:
    :param classifier:
    :param cv_num:
    :param random:
    :return:
    """
    result = list()
    for train_index, test_index in cv_index(x.shape[0], cv_num=cv_num, random=random):
        train_x, train_y = x[train_index], y[train_index]
        test_x, test_y = x[test_index], y[test_index]
        result.append(fit_and_score(train_x, train_y, test_x, test_y, classifier))
    return result


def fit_and_score_on_three_task(train_data_x, train_data_y, test_data_x, test_data_y, classifier):
    """
    fit train_data used classifier, and score in test_data
    on age, gender, education
    :param train_data_x:
    :param train_data_y: (instance, n_task)
    :param test_data_x:
    :param test_data_y: (instance, n_task)
    :param classifier:
    :return:
    """
    assert train_data_x.shape[0] == train_data_y.shape[0]
    assert test_data_x.shape[0] == test_data_y.shape[0]
    assert train_data_y.shape[1] == test_data_y.shape[1]
    score_list = list()
    for task in xrange(train_data_y.shape[1]):
        score = fit_and_score(train_data_x, train_data_y[:, task], test_data_x, test_data_y[:, task], classifier)
        score_list.append(score)
    score_list.append(np.mean(score_list))
    return score_list


def cv_index(num_instance, cv_num=10, random=True):
    """
    Generate CV Indexs
    :param num_instance:
    :param cv_num:
    :param random:
    :return:
    """
    indexs = np.arange(num_instance)
    if random:
        np.random.permutation(indexs)
    for cv_i in xrange(cv_num):
        single_cv = num_instance / cv_num

        # Generate Indexs
        test_index = indexs[np.arange(cv_i * single_cv, cv_i * single_cv + single_cv)]
        if cv_i == 0:
            train_index = indexs[np.arange(single_cv, num_instance)]
        elif cv_i == cv_num - 1:
            train_index = indexs[np.arange(0, num_instance - single_cv)]
        else:
            train_index = indexs[np.concatenate([np.arange(cv_i * single_cv),
                                                 np.arange(cv_i * single_cv + single_cv, num_instance)])]
        yield train_index, test_index


def cv_train_test(x, y, classifier, cv_num=10, random=True):
    """
    CV Train Test
    :param x:
    :param y:
    :param classifier:
    :param cv_num:
    :param random:
    :return:
    """
    result = list()
    for train_index, test_index in cv_index(x.shape[0], cv_num=cv_num, random=random):
        train_x, train_y = x[train_index], y[train_index]
        test_x, test_y = x[test_index], y[test_index]
        result.append(fit_and_score_on_three_task(train_x, train_y, test_x, test_y, classifier))
    return result


def feature_merge(x1, x2):
    """
    Merge Two Feature Matrix
    :param x1: (instances, feature1)
    :param x2: (instances, feature2)
    :return:
    """
    assert x1.shape[0] == x2.shape[0]
    from scipy.sparse import hstack
    return hstack([x1, x2])


def get_sgd_classifier_from_args(args):
    """
    Get a SGD Classifier from args
    :param args:
    :return:
    """
    from sklearn.linear_model import SGDClassifier
    return SGDClassifier(loss=args.sgd_loss,  # ‘hinge’, ‘log’, ‘modified_huber’, ‘squared_hinge’, ‘perceptron’
                         penalty=args.sgd_penalty,  # ‘none’, ‘l2’, ‘l1’, or ‘elasticnet’
                         n_iter=args.n_iter,
                         shuffle=args.shuffle,
                         alpha=args.alpha,  # Constant that multiplies the regularization term. Defaults to 0.0001
                         )


def get_nb_classifier_from_args(args):
    from sklearn.naive_bayes import MultinomialNB
    return MultinomialNB(alpha=args.alpha,  # Additive (Laplace/Lidstone) smoothing parameter (0 for no smoothing).
                         )


def get_classifier_from_args(args):
    if args.classifier.low() == "sgd":
        return get_sgd_classifier_from_args(args)
    elif args.classifier.low() == "nb":
        return get_nb_classifier_from_args(args)
    else:
        raise NotImplementedError


if __name__ == "__main__":
    pass
