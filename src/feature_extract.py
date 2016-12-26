# -*- coding: utf-8 -*-
# Feature Methods
# 抽取传统特征 Binary TF IDF TFIDF


import numpy as np
from arguments import add_feature_arg_parse


def ngram(query, n):
    """
    generate n gram str
    :param query:
    :param n:
    :return:
    """
    words = query.split(' ')
    output = list()
    for i in range(len(words) - n + 1):
        output.append(input[i:i + n])
    return output


def parse_data_line(line, train=True, gram_range=(1, 1)):
    """
    Parse a data in one line
    :param line:
    :param train:
    :param gram_range:
    :return:
    """
    att = line.strip().split("\t")
    word_list = list()
    if train:
        labels = [int(att[1]), int(att[2]), int(att[3])]
        queries = att[4:]
    else:
        labels = [-1, -1, -1]
        queries = att[1:]
    for q in queries:
        idxs = q.split()
        for gram in xrange(gram_range[0], gram_range[1] + 1):
            for i in range(len(idxs) - gram + 1):
                word_list.append("_".join(idxs[i:i + gram]))
    return labels, word_list


def read_data_file(filename, train=True, gram_range=(1, 1), cf=1):
    """
    Read Raw CCF Data File
    :param filename:
    :param train:
    :param gram_range:
    :param cf:
    :return:
    """
    label_list = list()
    queries = list()
    word_cf_count = dict()
    for line in open(filename, 'r'):
        l, q = parse_data_line(line, train=train, gram_range=gram_range)
        label_list.append(l)
        queries.append(q)
    for q in queries:
        for word in q:
            if word not in word_cf_count:
                word_cf_count[word] = 1
            else:
                word_cf_count[word] += 1
    for key in word_cf_count.keys():
        if word_cf_count[key] < cf:
            word_cf_count.pop(key)
    new_queries = list()
    for q in queries:
        new_word = list()
        for word in q:
            if word in word_cf_count:
                new_word.append(word)
        new_queries.append(" ".join(new_word))
    y = np.array(label_list, dtype=np.int32)
    return new_queries, y


def feature_extract(input_filename, gram=1, mode='tf', max_df=1.0, min_df=0.0, cf=1):
    """
    Feature Extract
    :param input_filename:
    :param gram: 1 2 ...
    :param mode: binary tf tfidf idf
    :param max_df:
    :param min_df:
    :param cf:
    :return:
    """
    from sklearn.feature_extraction.text import TfidfTransformer, CountVectorizer
    x_text, y = read_data_file(input_filename, train=True, gram_range=(1, gram), cf=cf)
    if mode == 'binary':
        feature_extractor = CountVectorizer(ngram_range=(1, 1), max_df=max_df,
                                            min_df=min_df, binary=False)
        x = feature_extractor.fit_transform(x_text)
    elif mode == 'tf':
        feature_extractor = CountVectorizer(ngram_range=(1, 1), max_df=max_df,
                                            min_df=min_df, binary=True)
        x = feature_extractor.fit_transform(x_text)
    elif mode == 'tfidf':
        feature_extractor1 = CountVectorizer(ngram_range=(1, 1), max_df=max_df,
                                             min_df=min_df, binary=False)
        x = feature_extractor1.fit_transform(x_text)
        feature_extractor2 = TfidfTransformer()
        x = feature_extractor2.fit_transform(x)
    elif mode == 'idf':
        feature_extractor1 = CountVectorizer(ngram_range=(1, 1), max_df=max_df,
                                             min_df=min_df, binary=True)
        x = feature_extractor1.fit_transform(x_text)
        feature_extractor2 = TfidfTransformer()
        x = feature_extractor2.fit_transform(x)
    else:
        raise NotImplementedError
    return x, y


def feature_extract_to_file(input_filename, output_filename, gram=1, mode='tf', max_df=1.0, min_df=0.0, cf=1):
    """
    Feature Extract -- Write to Sklearn Joblib File Format
    :param input_filename:
    :param output_filename:
    :param gram: 1 2 ...
    :param mode: binary tf tfidf idf
    :param max_df:
    :param min_df:
    :param cf:
    :return:
    """
    from sklearn.externals import joblib
    x, y = feature_extract(input_filename, gram=gram, mode=mode, max_df=max_df, min_df=min_df, cf=cf)
    joblib.dump((x, y), output_filename)
    return x, y


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


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', dest='input_file', type=str, help='Input File')
    parser.add_argument('-o', '--output', dest='output_file', type=str, help='Output File')
    add_feature_arg_parse(parser)
    parser.add_argument('-r', '--recommend-name', dest='recommend_name', action='store_true',
                        help='Just Recommend a Name')
    parser.set_defaults(recommend_name=False)
    args = parser.parse_args()
    if args.mode not in ['tf', 'binary', 'idf', 'tfidf']:
        raise NotImplementedError
    if args.recommend_name:
        print "%dgram_%s_maxdf%.2f_mindf%.2f_cf%d" % (args.gram, args.mode, args.max_df, args.min_df, args.cf)
        exit(1)
    feature_extract_to_file(input_filename=args.input_file,
                            output_filename=args.output_file,
                            gram=args.gram, mode=args.mode,
                            max_df=args.max_df, min_df=args.min_df,
                            cf=args.cf)
