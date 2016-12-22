from feature_extract import feature_extract
from sklearn.naive_bayes import MultinomialNB
from model import cv_train_test
import numpy as np

filenames = ["../data/processed/2w/2w.data.TRAIN",
             "../data/processed/2w/2w.data.num.TRAIN",
             "../data/processed/2w/2w.data.alpha.TRAIN",
             "../data/processed/2w/2w.data.url.TRAIN",
             "../data/processed/10w/10w.data.TRAIN",
             "../data/processed/10w/10w.data.num.TRAIN",
             "../data/processed/10w/10w.data.alpha.TRAIN",
             "../data/processed/10w/10w.data.url.TRAIN",

             ]

classifier = MultinomialNB()

for filename in filenames:
    x, y = feature_extract(filename)
    result = cv_train_test(x, y, classifier)
    result = np.array(result)
    print np.mean(result, axis=0)
