#-------*-coding:utf-8-*-------
import string
from svm import *
from crossvalidation import *


def frange(x, y, jump):
    if jump > 0:
        while x < y:
            yield x
            x += jump
    else:
        while x > y:
            yield x
            x += jump


def grid_search(instances, labels, types='regress', c_begin=-10, c_end=10, c_step=1, g_begin=-10, g_end=10, g_step=1, fold=3):
    '''Used for search the param of this function
            type :regress
                  classify
       and return a tuple as (C,Gamma)
    '''
    problem = svm_problem(labels, instances)
    size = len(labels)
    best_c = c_begin
    best_g = g_begin
    min_error = 1000000000.0

    if types is "regress":
        print  "here"
        for c in xrange(c_begin, c_end, c_step):
            for g in xrange(g_begin, g_end, g_step):
        
                print "c is %f,g is %f" % (c, g)
                param = svm_parameter(
                    C=2.0 ** c, gamma=2.0 ** g, svm_type=EPSILON_SVR)
                temp_error = do_cross_validation(
                    instances, labels, param, fold)
                if min_error > temp_error:
                    min_error = temp_error
                    best_g = g
                    best_c = c
    elif types == "classify":
        max_presicion = 0
        for c in xrange(c_begin, c_end, c_step):
            for g in xrange(g_bein, g_end, g_step):

                param = svm_parameter(
                    kernal_type=RBF, C=c, gamma=g, svm_type=C_SVC)
                temp_presicion = do_cross_validation(
                    instances, labels, param, fold)
                if max_presicion < temp_presicion:
                    max_presicion = temp_presicion
                    best_g = g
                    best_c = c
    else:
        print "please input the right type of the svm"
        best_c = -100
        best_g = -100
    print "good"
    return (best_c, best_g)
