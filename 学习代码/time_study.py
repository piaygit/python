# -*-coding=utf-8 -*-
__author__ = 'piay'
import time
def get_struct_time():
    '''
    可以使用list或者字符串格式化
     tm_year-->年
     tm_mon-->月
     tm_mday-->日
     tm_hour-->时
     tm_min-->分
     tm_sec-->秒
     tm_wday--> 0 - 6（0表示周1）
     tm_yday-->一年中的第几天（1-366）
     tm_isdst-->是否是夏令时，默认为-1
    :return:-->time.struct_time(tm_year=2016, tm_mon=6, tm_mday=16,
    tm_hour=23, tm_min=29, tm_sec=13, tm_wday=3, tm_yday=168, tm_isdst=0)
    '''
    return time.localtime()


#time.localtime([sec]) 将一个时间戳转换为当前时区的struct)_time,sec参数不提供的话，则以当前时间为标准
print time.localtime()
#time.gtime([sec]) 同localtime类似只是转换为utc时区的时间
print time.gmtime()
 #返回当前时间的时间戳
print time.time()
# time.mktime 将struct_time转换为时间戳
print time.mktime(time.localtime())