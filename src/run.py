import os
from feature_extract import feature_extract_to_file
from classifier import get_classifier_from_args
from model import cv_train_test
from arguments import add_feature_arg_parse, add_classifier_arg_parse, add_data_arg_parse, get_data_information, \
    get_feature_information, get_classifier_information
import numpy as np


def get_data_from_args(_args):
    from sklearn.externals import joblib
    if _args.data not in ['2w', '10w']:
        raise NotImplementedError
    if _args.mode not in ['tf', 'binary', 'idf', 'tfidf']:
        raise NotImplementedError
    feature_file_name = "../data/feature/%s/%dgram_%s_maxdf%.2f_mindf%.2f_cf%d" % (_args.data, _args.gram, _args.mode,
                                                                                   _args.max_df, _args.min_df, _args.cf)
    if not os.path.isfile(feature_file_name):
        if _args.data == '2w':
            input_file = "../data/processed/2w/2w.data.TRAIN"
        elif _args.data == '10w':
            input_file = "../data/processed/10w/10w.data.TRAIN"
        else:
            raise NotImplementedError
        print "Feature Extract to %s" % feature_file_name
        return feature_extract_to_file(input_filename=input_file,
                                       output_filename=feature_file_name,
                                       gram=_args.gram, mode=_args.mode,
                                       max_df=_args.max_df, min_df=_args.min_df,
                                       cf=_args.cf)
    else:
        print "Feature Load from %s" % feature_file_name
        return joblib.load(feature_file_name)


def main():
    import argparse
    parser = argparse.ArgumentParser()
    add_data_arg_parse(parser)
    add_feature_arg_parse(parser)
    add_classifier_arg_parse(parser)
    args = parser.parse_args()
    x, y = get_data_from_args(args)
    classifier = get_classifier_from_args(args)
    print "[Data]", get_data_information(args)
    print "[Feature]", get_feature_information(args)
    print "[Classifier]", get_classifier_information(args)
    if args.task == "all":
        result = cv_train_test(x, y, classifier, cv_num=args.cv_num, random=args.cv_random)
    elif args.task == "age":
        result = cv_train_test(x, y[:, 0], classifier, cv_num=args.cv_num, random=args.cv_random)
    elif args.task == "gender":
        result = cv_train_test(x, y[:, 1], classifier, cv_num=args.cv_num, random=args.cv_random)
    elif args.task == "education":
        result = cv_train_test(x, y[:, 2], classifier, cv_num=args.cv_num, random=args.cv_random)
    else:
        raise NotImplementedError
    print np.mean(result, axis=0)


if __name__ == "__main__":
    main()
