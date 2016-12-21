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
    for cv_index in xrange(cv_num):
        single_cv = num_instance / cv_num

        # Generate Indexs
        test_index = indexs[np.arange(cv_index * single_cv, cv_index * single_cv + single_cv)]
        if cv_index == 0:
            train_index = indexs[np.arange(single_cv, num_instance)]
        elif cv_index == cv_num - 1:
            train_index = indexs[np.arange(0, num_instance - single_cv)]
        else:
            train_index = indexs[np.concatenate([np.arange(cv_index * single_cv),
                                                 np.arange(cv_index * single_cv + single_cv, num_instance)])]
        yield train_index, test_index


def cv_train_test(x, y, classifier, cv_num=10, random=True):
    for train_index, test_index in cv_index(x.shape[0], cv_num=cv_num, random=random):
        train_x, train_y = x[train_index], y[train_index]
        test_x, test_y = x[test_index], y[test_index]
        print fit_and_score_on_three_task(train_x, train_y, test_x, test_y, classifier)


def feature_merge(x1, x2):
    pass
