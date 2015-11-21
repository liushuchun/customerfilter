#-----*-coding:utf-8-*-------

Q1_FEATURE_MAP = {
    '10个': 1,
    '11个': 0,
    'null':-1,
}

# answers
Q2_FEATURE_MAP = {
    '最后的提现奖励': 1,
    '想学习理财': 2,
    '对互联网感兴趣': 3,
    '朋友推荐': 4,
    'null':-1,
    'other':-1,
}

# investment types
Q3_FEATURE_MAP = {
    '投资': 1,
    '比特': 2,
    '赚': 3,
    '彩票': 4,
    '翻': 5,
    '股票': 6,
    '基金': 7,
    '房': 8,
    '电子':9,
    'other': 20,
    'null':-1
}

ADDRESS_FEATURE_MAP = {
    '陆家嘴': 1,
    '浦东': 2,
    '淮海': 3,
    '徐汇': 4,
    '淮海': 5,
    '上海': 6,
    '海淀区': 7,
    '北京': 8,
    '深圳': 9,
    '杭州': 10,
    'other': 20,  # other locations
}

IS_TEL_MAP = {
    'True': 1,
    'False': 0
}

IS_IPHONE_MAP = {
    'True': 1,
    'False': 0
}

EMAIL_MAP = {
    'qq': 1,
    'koolla': 2,
    '163': 3,
    '139': 4,
    'richemont': 5,
    '126': 6,
    'pingan': 7,
    'hotmail': 8,
    'wacai': 9,
    'gmail': 10,
    'sina': 11,
    'mit': 12,
    'foxmail': 13,
    'outlook': 14,
    'live': 15,
    'pingan': 16,
    'outlook':17,
    'yeah': 18,
    '.': 0,
    'null':-1,
    'other':-2,

}  # 0 represent others
