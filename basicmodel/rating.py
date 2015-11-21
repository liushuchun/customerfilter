#-----*-coding:utf-8-*------
'''
	rating.py
    this module provide with the basic rate method for the manager to rank the pre launch users
'''


from tabletoexcel import *
from getusers import *
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import math


def calculate_score(users, weights):
    '''calculate the score of each user
       and return with a sorted and scored tables
    '''
    new_users = []
    for user in users:
        score = 0
        item = user
        email_score = ScoreFactory.create('email', user["email"])
        q1_score = ScoreFactory.create('q1', user['q1'])
        q2_score = ScoreFactory.create('q2', user['q2'])
        q3_score = ScoreFactory.create('q3', user["q3"])
        duration_score = ScoreFactory.create('duration', user['duration'])
        iphone_score = ScoreFactory.create('iphone', user['duration'])
        address_score = ScoreFactory.create('address', user["address"])
        score = weights[0] * email_score + weights[1] * q1_score + weights[2] * q2_score \
            + weights[3] * q3_score + weights[4] * duration_score\
            + weights[5] * iphone_score + weights[6] * address_score

        item["score"] = score
        new_users.append(item)

    return new_users


def main():
    ''''the main process of the model'''

    users = get_users()
    weights = [0.05, 0.05, 0.1, 0.4, 0.1, 0.15, 0.15]  # email q1 q2 q3
    new_users = calculate_score(users, weights)

    new_users.sort(key=lambda obj: obj.get('score'), reverse=True)
    table_to_excel(new_users)


class ScoreFactory:

    """
    This class provide some method to rate for the items
    """
    @staticmethod
    def create(col_name, item):
        score = 0
        if len(str(item)) == 0:
            score = -10
            return score

        if col_name == 'email':
            score = ScoreFactory._email_rating(item)
        elif col_name == "q1":
            score = ScoreFactory._first_question_rating(item)
        elif col_name == "q2":
            score = ScoreFactory._second_question_rating(item)
        elif col_name == "q3":
            score = ScoreFactory._third_question_rating(item)
        elif col_name == "duration":
            score = ScoreFactory._duration_rating(item)
        elif col_name == "iphone":
            score = ScoreFactory._iphone_rating(item)
        elif col_name == "address":
            score = ScoreFactory._address_rating(item)
        else:
            score = ScoreFactory._others(item)
        # print "col:%s,score:%d" % (col_name,score)
        return score

    @staticmethod
    def _email_rating(item):
        mail_rank_map = {"qq": 50,
                         "163": 60,
                         "edu": 70,
                         "126": 70,
                         "foxmail": 90,
                         "outlook": 100,
                         "gmail": 100,
                         "hotmail": 100,
                         "live": 100,
                         "yahoo": 100,
                         'sc.':110}
        score = 50
        for key, value in mail_rank_map.items():
            if item.find(key) >= 0:
                return value
        return score

    @staticmethod
    def _first_question_rating(item):
        score = 50
        if str(item).find("10") >= 0:
            score = 100
        else:
            score = 0
        return score

    @staticmethod
    def _second_question_rating(item):
        score = 50

        if str(item).find("最后的") != -1:
            score = 40
        elif str(item).find("理财") != -1:
            score = 100
        elif str(item).find("互联网") != -1:
            score = 80
        elif str(item).find("朋友") != -1:
            score = 60

        return score

    @staticmethod
    def _third_question_rating(item):
        score = 50
        if len(item) <= 4:
            score = -30
            return score
        elif len(item) < 8:
            score = 20
        else:
            score = 60
        if item.find("股") != -1 or item.find("房") != -1:
            score = score + 40
        elif item.find("基金") != -1 or item.find("债券") != -1:
            score = score + 20
        elif item.find("比特") != -1 or item.find("投资") != -1:
            score = score + 10
        elif item.find("没") != -1 or item.find("余额") != -1:
            score = score - 10

        return score

    @staticmethod
    def _duration_rating(item):
        x = float(item)
        score = -(x - 400.0) * (x - 400.0) / 900.0 + 100
        if score < 0:
            score = 0
        return int(score)

    @staticmethod
    def _iphone_rating(item):

        if item == 1:
            score = 100
        else:
            score = 0
        return score

    @staticmethod
    def _address_rating(item):
        if len(item) == 0:
            score = 0
        if item.find("浦东") != -1 or item.find("陆家嘴") != -1:
            score = 100
        elif item.find("上海") != -1:
            score = 80
        else:
            score = 60

        return score

    @staticmethod
    def _others(item):
        return 0


if __name__ == '__main__':
    '''For test the function of the factory'''
    a = ScoreFactory._duration_rating(500)
    # runing()
    # test the function of the email
    email_list = {"liu@gmail.com", "lius@outlook.com", "234@qq.com", "kankan@yahoo.com", "good@live.com", "ecnu@edu.com"}
    print "test the email:"
    for email in email_list:
        print "%s:%d" % (email, ScoreFactory._email_rating(email))
    # test the function of the q2
    q2_list = {"最后的神秘大礼", "想学习理财", "对互联网金融感兴趣", "朋友推荐"}
    for q in q2_list:
        print "%s:%d" % (q, ScoreFactory._second_question_rating(q))
    print ScoreFactory._iphone_rating(1)
    print ScoreFactory._iphone_rating(0)

    main()
