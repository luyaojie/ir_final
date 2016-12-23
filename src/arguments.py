def add_data_arg_parse(_parser):
    _parser.add_argument('-d', '--data', dest='data', type=str, default='2w',
                         help="Data Size: ['2w', '10w'], default is 2w")
    _parser.add_argument('-t', '--task', dest='task', type=str, default='all',
                         help="Task: ['age', 'gender', 'education', 'all'], default is all")
    _parser.add_argument('--cv-num', dest='cv_num', type=int, default=10,
                         help="Cross Validation Times")
    _parser.add_argument('--cv-random', dest='cv_random', action='store_true',
                         help='Random for Cross Validation, default is no random')
    _parser.set_defaults(cv_random=False)


def add_feature_arg_parse(_parser):
    _parser.add_argument('-g', '--gram', dest='gram', type=int, default=1, help='Gram Number')
    _parser.add_argument('-m', '--mode', dest='mode', type=str, default='tf',
                         help="Model: ['binary', 'tf', 'tfidf', 'idf'], default is 'tf'")
    _parser.add_argument('--max-df', dest='max_df', type=float, default=1.0,
                         help="Max Document Frequency, default is 1.0")
    _parser.add_argument('--min-df', dest='min_df', type=float, default=0.0,
                         help='Min Document Frequency, default is 0.0')
    _parser.add_argument('--cf', dest='cf', type=int, default=1, help='Min Corpus Frequency')


def add_classifier_arg_parse(_parser):
    _parser.add_argument('--classifier', dest='classifier', type=str, default='nb',
                         help="classifier: ['nb', 'sgd'], default is nb")
    _parser.add_argument('--nb-alpha', dest='nb_alpha', type=float, default=1.0,
                         help='Additive (Laplace/Lidstone) smoothing for NB, default is 1.0')
    _parser.add_argument('--sgd-alpha', dest='sgd_alpha', type=float, default=0.0001,
                         help='Constant that multiplies the regularization term, default is 0.0001')
    _parser.add_argument('--iter', dest='iter', type=int, default=5,
                         help='Iter num for SGD Classifier, default is 5')
    _parser.add_argument('--sgd-loss', dest='sgd_loss', type=str, default='loss',
                         help="SGD Loss ['hinge', 'log', 'modified_huber', 'squared_hinge', " +
                              "perceptron'], default is 'log'")
    _parser.add_argument('--sgd-shuffle', dest='sgd_shuffle', action='store_false',
                         help='Shuffle instances in Training SGD Classifier, default is shuffle')
    _parser.add_argument('--sgd-no-shuffle', dest='sgd_shuffle', action='store_false',
                         help='Shuffle instances in Training SGD Classifier, default is shuffle')
    _parser.set_defaults(sgd_shuffle=True)


def get_data_information(_args):
    return "data %s, task %s, cv-num %d, cv-random %s" % (_args.data, _args.task, _args.cv_num, _args.cv_random)


def get_feature_information(_args):
    return "gram %s, mode %s, max-df %.2f, min-df %.2f, cf %d" % (_args.gram, _args.mode, _args.max_df,
                                                                  _args.min_df, _args.cf)


def get_classifier_information(_args):
    if _args.classifier == "nb":
        return "classifier: nb, alpha %f" % _args.nb_alpha
    elif _args.classifier == "sgd":
        return "classifier: sgd, loss %s, alpha %f, iter %s, shuffle %s" % (_args.sgd_loss, _args.sgd_alpha,
                                                                            _args.iter, _args.sgd_shuffle)
    else:
        raise NotImplementedError
