#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
def get_check_code(str):
    #位数与因数对应关系
    relation = {1:7, 2:9, 3: 10, 4: 5, 5: 8, 6: 4, 7: 2, 8: 1, 9: 6, 10: 3, 11: 7, 12: 9,
                13: 10, 14: 5, 15: 8, 16: 4, 17: 2}
    m = 0
    #得到前17位的因数乘积之和
    for key in relation.keys():
        m+=int(str[key-1])*relation[key]
    m=m%11
    #余数与最后一位对应表
    last_num = {0: '1', 1: '0', 2: 'x', 3: '9', 4: '8', 5: '7', 6: '6', 7: '5', 8: '4', 9: '3', 10: '2'}
    return last_num[m]