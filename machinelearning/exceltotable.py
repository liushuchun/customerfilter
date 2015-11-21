#-*- coding:utf-8-*-
import xlrd
import sys
import xdrlib


def open_excel(file='import.xls'):
    '''Open the excel files'''
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception, e:
        print str(e)


def excel_to_table(file_name="import.xls"):
	'''This function help you to convert the excel to the user list'''
    data = xlrd.open_workbook(file_name)
    table = data.sheets()[0]
    nrows = table.nrows
    ncols = table.ncols
    col_names = table.row_values(0)

    user_list = []
    for index in xrange(1, nrows):
        row = table.row_values(index)
        if row:
            user = {}
            for i in range(len(col_names)):
                user[col_names[i]] = row[i]
            user_list.append(user)

    return user_list
  


if __name__=="__main__":
    user_list=excel_to_table("result.xls")
    print user_list
