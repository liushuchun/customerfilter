#-----coding:utf-8-*------
import os
import sys
from staticvalues import *
from validation import *
sys.path.append("..")
from basicmodel.rating import *
from basicmodel.tabletoexcel import *


def map_word(item, maps=None):
    '''General map function'''
    if isinstance(item, float) or isinstance(item, int):
        return item
    if maps is None:
        return item

    if len(str(item)) == 0:
        return maps["null"]
    if maps == IS_TEL_MAP:
        return phone_check(item)

    for key, value in maps.items():
        if item.find(key) != -1:
            return value
    return maps["other"]


def extract_features(user_list):
    '''Extracting the features in the tables;
    you need to provide the user_list of the user and the function 
    will return with a tuple(samples,labels)
    cols->index:
            src address q1     q2    q3  duration iphone tel email
            0     1      2     3     4      5        6    7    8
    '''
    samples = []
    labels = []
    for user in user_list:
        item = []
        item.append(user["src"])
        item.append(map_word(user["address"], ADDRESS_FEATURE_MAP))
        item.append(map_word(user["q1"], Q1_FEATURE_MAP))
        item.append(map_word(user["q2"], Q2_FEATURE_MAP))
        item.append(map_word(user["q3"], Q3_FEATURE_MAP))
        item.append(map_word(user["duration"]))
        item.append(map_word(user["iphone"], IS_IPHONE_MAP))
        item.append(map_word(user["tel"], IS_TEL_MAP))
        item.append(map_word(user["email"], EMAIL_MAP))
        score = user["score"]
        samples.append(item)
        labels.append(score)
        print 'user:%s' % (user)

        print 'item:%s' % (item)
    return (samples, labels)
