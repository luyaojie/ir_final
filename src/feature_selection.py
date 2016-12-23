# -*- coding: utf-8 -*-
# Feature Selection
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_selection import chi2
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import SelectPercentile
from sklearn.feature_selection import mutual_info_classif
import functools

def dataTransform(input_filename):
    counter = CountVectorizer()
    id=list()
    data = list()
    label_age = list()
    label_gender = list()
    label_education = list()
    with open(input_filename, "r") as fin:
        for line in fin:
            str = line.strip().split("\t")
            label_age.append(int(str[1]))
            label_gender.append(int(str[2]))
            label_education.append(int(str[3]))
            query_list = [q for q in str[4:]]
            data.append(" ".join(query_list))
    train_data_x = counter.fit_transform(data)
    labels = {'age': label_age, 'gender': label_gender, 'education': label_education}
    return id, train_data_x, labels


def filter(input_filename, label='age', filter='MI', mode='proportion', value=1.0):
    id,train_data_x, labels=dataTransform(input_filename)
    if filter=='chi2':
        train_data_x_new=computeChi2(train_data_x,labels[label],mode,value)
    if filter=='MI':
        train_data_x_new = computeMI(train_data_x, labels[label], mode, value)
    if filter=='IG':
        pass
    return train_data_x_new


def computeMI(train_data_x,label,mode='proportion', value=1.0):
    mi=functools.partial(mutual_info_classif,n_neighbors=2)
    print '--'
    if mode=='proportion':
        Selecter=SelectPercentile(mi,value)
    if mode=='num':
        Selecter = SelectKBest(mi, value)
    train_data_x_new=Selecter.fit_transform(train_data_x,label)
    return train_data_x_new

def computeIG(input_filename,IG_filename):
    # Written by Roger
    pass

def computeChi2(train_data_x,label,mode='proportion', value=1.0):
    if mode=='proportion':
        Selecter=SelectPercentile(chi2,value)
    if mode=='num':
        Selecter = SelectKBest(chi2, value)
    train_data_x_new=Selecter.fit_transform(train_data_x,label)
    return train_data_x_new


