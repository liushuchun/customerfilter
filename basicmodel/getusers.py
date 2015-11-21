#----*-coding:utf-8-*----
from dbutils import *


def db():
    '''basic database configuration'''
    return Connection(host='', database='', user='root', password='')

db = db()


def get_users():
    '''get the user list from the database'''
    sql = 'select * from lead2'
    user_table = db.query(sql)
    #print user_table
    return user_table


print get_users()
