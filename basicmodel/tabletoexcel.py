#-*-coding:utf8 -*-
#import xlrd

from pyExcelerator import *


def table_to_excel(user_list, file_name="result.xls"):
    '''This function can output the user_list to the excel files'''
    work_book = Workbook()
    work_sheet = work_book.add_sheet("solution")
    key_col_map = {}
    for col, key in enumerate(user_list[0]):
        work_sheet.write(0, col, key)
        key_col_map[key] = col

    for cursor, user in enumerate(user_list):
        for key, value in user.items():
            work_sheet.write(cursor + 1, key_col_map[key],  str(value).decode("utf-8"))

    work_book.save(file_name)


if __name__ == "__main__":
    '''For test the function'''
    test_list = []
    item1 = {}
    item1["test"] = "good"
    item1["number"] = 10
    item2 = {"test": "bad",
             "number": 9
             }
    test_list.append(item1)
    test_list.append(item2)
    table_to_excel(test_list)
