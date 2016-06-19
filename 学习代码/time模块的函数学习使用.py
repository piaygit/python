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


# time.localtime([sec]) 将一个时间戳转换为当前时区的struct)_time,sec参数不提供的话，则以当前时间为标准
print time.localtime()
# ----->time.struct_time(tm_year=2016, tm_mon=6, tm_mday=19, tm_hour=12, tm_min=57, tm_sec=17, tm_wday=6, tm_yday=171, tm_isdst=0)


#time.gtime([sec]) 同localtime类似只是转换为utc时区的时间
print time.gmtime()
#----->time.struct_time(tm_year=2016, tm_mon=6, tm_mday=19, tm_hour=4, tm_min=57, tm_sec=17, tm_wday=6, tm_yday=171, tm_isdst=0)


#返回当前时间的时间戳
print time.time()
#----->1466312237.8

# time.mktime 将struct_time转换为时间戳
print time.mktime(time.localtime())
#----->1466312237.0


#将一个struct_time(默认为当时时间)，转换成字符串
print time.asctime()
#---->Sun Jun 19 12:57:17 2016


# 把一个时间戳（按秒计算的浮点数）转化为time.asctime()的形式。 如果参数未给或者为None的时候，
# 将会默认time.time()为参数。它的作用相当于 asctime(localtime(secs))。
print time.ctime()
# -->Sun Jun 19 14:33:26 2016

#time.clock() 函数有两个功能：第一次调用的时候返回的是程序运行的实际时间，第一次调用以后的调用，返回的是自第一次调用后，到
#此次调用的时间间隔
time.sleep(1)
print 'clock1:%s' % time.clock()
time.sleep(1)
print 'clock2:%s' % time.clock()
time.sleep(1)
print 'clock3:%s' % time.clock()
# 输出:clock1:2.93333370582e-06 --->输出程序运行时间
#     clock2:1.00065301596 -->输出与第一个clock的时间间隔
#     clock3:2.00075212073 -->输出与第一个clock的时间间隔


# 线程推辞时间运行，参数单位为秒，比如sleep1秒
# 休眠的时间并非十分精确，有一个浮动值,参数可以是一个浮点数，可以保证精确到0.1s
time.sleep(1.5)

# time.strftime()
'''
strftime(format[, tuple]) -> string
将指定的struct_time(默认为当前时间)，根据指定的格式化字符串输出
python中时间日期格式化符号：
  %y 两位数的年份表示（00-99）
  %Y 四位数的年份表示（000-9999）
  %m 月份（01-12）
  %d 月内中的一天（0-31）
  %H 24小时制小时数（0-23）
  %I 12小时制小时数（01-12）
  %M 分钟数（00=59）
  %S 秒（00-59）

  %a 本地简化星期名称
  %A 本地完整星期名称
  %b 本地简化的月份名称
  %B 本地完整的月份名称
  %c 本地相应的日期表示和时间表示
  %j 年内的一天（001-366）
  %p 本地A.M.或P.M.的等价符
  %U 一年中的星期数（00-53）星期天为星期的开始
  %w 星期（0-6），星期天为星期的开始
  %W 一年中的星期数（00-53）星期一为星期的开始
  %x 本地相应的日期表示
  %X 本地相应的时间表示
  %Z 当前时区的名称
  %% %号本身
'''
print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
# --->2016-06-19 14:26:18

# time.strptime()
'''
strptime(string, format) -> struct_time
将时间字符串根据指定的格式化符转换成数组形式的时间
'''
print time.strptime('2016 9 25 10:22:32','%Y %m %d %H:%M:%S')
# -->time.struct_time(tm_year=2016, tm_mon=9, tm_mday=25, tm_hour=10, tm_min=22, tm_sec=32, tm_wday=6, tm_yday=269, tm_isdst=-1)

