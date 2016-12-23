import numpy as np
from feature_extract import read_data_file
from gensim.models import Word2Vec
from arguments import add_data_arg_parse, get_data_information, add_embedding_feature_arg_parse
from arguments import add_classifier_arg_parse, get_embedding_feature_information, get_classifier_information
from classifier import get_classifier_from_args
from model import cv_train_test
import os
import math


def embedding_feature_extract(input_file, embedding_file, pooling='mean'):
    import cPickle
    queries, y = read_data_file(input_file)
    if pooling not in ['mean', 'max', 'idf']:
        raise NotImplementedError
    model = Word2Vec.load_word2vec_format(embedding_file, binary=True)
    x = list()
    if pooling in ['mean', 'max']:
        for i in xrange(len(queries)):
            embedding_list = list()
            for word in queries[i].split():
                embedding_list.append(model[word.decode("utf8")])
            if pooling == 'mean':
                x.append(np.mean(embedding_list, axis=0))
            else:
                x.append(np.max(embedding_list, axis=0))
        x = np.array(x)
        return x, y
    elif pooling == "idf":
        idf_file = input_file + ".idf"
        if not os.path.isfile(idf_file):
            idf_dict = dict()
            for i in xrange(len(queries)):
                word_set = set(queries[i].split())
                for word in word_set:
                    if word not in idf_dict:
                        idf_dict[word] = 1
                    else:
                        idf_dict[word] += 1
            # Calc Idf Value
            document_num = float(len(queries))
            for word in idf_dict.iterkeys():
                idf_dict[word] = math.log(document_num / idf_dict[word])
            with open(idf_file, 'wb') as out:
                cPickle.dump(idf_dict, out)
        else:
            with open(idf_file, 'rb') as fin:
                idf_dict = cPickle.load(fin)
        for i in xrange(len(queries)):
            embedding_list = list()
            for word in queries[i].split():
                weight = 0
                if word in idf_dict:
                    weight = idf_dict[word]
                embedding_list.append(model[word.decode("utf8")] * weight)
            x.append(np.mean(embedding_list, axis=0))
        x = np.array(x)
        return x, y
    else:
        raise NotImplementedError


def embedding_feature_extract_file(input_file, embedding_file, output_file, pooling='mean'):
    from sklearn.externals import joblib
    x, y = embedding_feature_extract(input_file, embedding_file, pooling=pooling)
    joblib.dump((x, y), output_file)
    return x, y


def get_embedding_feature(_args):
    from sklearn.externals import joblib
    if _args.data not in ['2w', '10w']:
        raise NotImplementedError
    if _args.pooling not in ['mean', 'max', 'idf']:
        raise NotImplementedError
    embedding_name = _args.embedding.split(os.sep)[1].replace(".bin", "")
    feature_file_name = "../data/feature/%s/%s.%s" % (_args.data, embedding_name, _args.pooling)
    if not os.path.isfile(feature_file_name):
        if _args.data == '2w':
            input_file = "../data/processed/2w/2w.data.TRAIN"
        elif _args.data == '10w':
            input_file = "../data/processed/10w/10w.data.TRAIN"
        else:
            raise NotImplementedError
        print "Feature Extract to %s" % feature_file_name
        return embedding_feature_extract_file(input_file=input_file,
                                              embedding_file=_args.embedding,
                                              output_file=feature_file_name,
                                              pooling=_args.pooling)
    else:
        print "Feature Load from %s" % feature_file_name
        return joblib.load(feature_file_name)


def main():
    import argparse
    parser = argparse.ArgumentParser()
    add_data_arg_parse(parser)
    add_embedding_feature_arg_parse(parser)
    add_classifier_arg_parse(parser)
    args = parser.parse_args()
    x, y = get_embedding_feature(args)
    classifier = get_classifier_from_args(args)
    print "[Data]", get_data_information(args)
    print "[Feature]", get_embedding_feature_information(args)
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
