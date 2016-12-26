# -*- coding: utf-8 -*-
# 从命令行参数生成一个分类器


def get_sgd_classifier_from_args(_args):
    """
    Get a SGD Classifier from args
    :param _args:
    :return:
    """
    from sklearn.linear_model import SGDClassifier
    if _args.sgd_loss not in ['hinge', 'log', 'modified_huber', 'squared_hinge', 'perceptron']:
        raise NotImplementedError
    return SGDClassifier(loss=_args.sgd_loss,  # 'hinge', 'log', 'modified_huber', 'squared_hinge', 'perceptron'
                         n_iter=_args.iter,
                         shuffle=_args.sgd_shuffle,
                         alpha=_args.sgd_alpha,  # Constant that multiplies the regularization term. Defaults to 0.0001
                         )


def get_nb_classifier_from_args(_args):
    from sklearn.naive_bayes import MultinomialNB
    return MultinomialNB(alpha=_args.nb_alpha,  # Additive (Laplace/Lidstone) smoothing parameter (0 for no smoothing).
                         )


def get_classifier_from_args(_args):
    if _args.classifier.lower() == "sgd":
        return get_sgd_classifier_from_args(_args)
    elif _args.classifier.lower() == "nb":
        return get_nb_classifier_from_args(_args)
    else:
        raise NotImplementedError
