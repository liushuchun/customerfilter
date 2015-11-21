#----*-coding:utf-8-*-------
from gridsearch import *
from getfeatures import *
from libsvm.svm import *
import sys
reload(sys)
sys.path.append("..")
sys.setdefaultencoding('utf-8')
from basicmodel.getusers import *
from basicmodel.rating import *
from basicmodel.tabletoexcel import *


def main():
    '''The main process of the data training'''
    print "The AI algorithm is running now."
    print "Import datas from the remmote database."
    user_list = get_users()
    weights = [0.05, 0.05, 0.1, 0.4, 0.1, 0.15, 0.15]
    sorted_user_list = calculate_score(user_list, weights)
    print "Sort the user list."
    sorted_user_list.sort(key=lambda obj: obj.get('score'), reverse=True)
    print "Extract features from the user list."
    (instances, labels) = extract_features(sorted_user_list)
    print sorted_user_list[0].keys()
    print 'The instances:'
    print instances
    print 'Grid search for the best parameters.'
    (c, g) = grid_search(instances, labels, types='regress')
    print "The best c is %f , best g is %f" % (c, g)
    # Build the model of the train data
    print 'Build the model now.'
    problem = svm_problem(labels, instances)
    size = len(instances)
    c = c + 10
    #c = 100
    # g=1
    param = svm_parameter(C=2.0 ** c, gamma=2.0 ** g, svm_type=EPSILON_SVR)
    model = svm_model(problem, param)
    pred_labels = []
    print 'Use the model to predict'
    for instance in instances:
        label = model.predict(instance)
        pred_labels.append(label)

    for i in xrange(0, size):
        sorted_user_list[i]["ML_score"] = pred_labels[i]
    print 'Output the data to the excel'
    table_to_excel(sorted_user_list)
    print "Please check the file result.xls"


if __name__ == "__main__":
    main()
