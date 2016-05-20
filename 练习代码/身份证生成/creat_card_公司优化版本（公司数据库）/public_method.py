#-*- coding=utf-8 -*-
import sys,time,random,MySQLdb
reload(sys)
sys.setdefaultencoding('utf-8')
def get_last_number(args):
    '''

    :param args: 传入身份证前17位
    :return: 返回最后一位的str字符
    '''
    # 位数与因数对应关系
    relation = {1: 7, 2: 9, 3: 10, 4: 5, 5: 8, 6: 4, 7: 2, 8: 1, 9: 6, 10: 3, 11: 7, 12: 9,
                13: 10, 14: 5, 15: 8, 16: 4, 17: 2}
    m = 0
    for key in relation.keys():
        m+=int(args[key-1])*relation[key]
    m=m%11
    # 余数与最后一位对应表
    last_num = {0: '1', 1: '0', 2: 'x', 3: '9', 4: '8', 5: '7',
                6: '6', 7: '5', 8: '4', 9: '3', 10: '2'}
    return last_num[m]

def get_random_date():
    '''

    :return: date:随机生成的6位出生年月日
    '''
    now=long(time.time())#获取当前的unix时间戳，转换为long类型
    date=random.randint(0,now) #从1970至今生成一个随机的unix时间戳
    date=time.gmtime(date)#转换为普通时间类型
    date=str(time.strftime("%Y%m%d",date))
    return date
def content_mysql():
    '''

    :return: 返回一个数据库连接
    '''
    try:
        conn=MySQLdb.Connect(
            port=3306,
            user="root",
            passwd="",
            charset="utf8",
            db="spider"
        )
    except:
        print "请检查你的数据库连接"
    return conn