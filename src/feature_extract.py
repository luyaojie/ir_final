# -*- coding: utf-8 -*-
# Feature Methods


# Feature Extractor Model
# Save Load


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


def featureExtract(input_filename, output_filename, gram=1, mode='tf'):
    """
    Feature Extract -- Write to Sklearn Joblib File Format
    :param input_filename:
    :param output_filename:
    :param gram: 1 2 ...
    :param mode: binary tf tfidf idf doc2vec
    :return:
    """
    pass


"""
inputfile
    Text File

OutpuFile
    Matrix
    data/2w/2w.<feature_name>.train
        Matrix (instance_num, feature_num) # scipy csr
        Matrix (instance_num, feature_num) # Numpy -> array
data/2w/2w.<feature_name>.model

class featureextractor
"""
