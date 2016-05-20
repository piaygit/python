#-*- coding=utf-8 -*-
import os
def search(s,args):
    '''

    :param s: 目录
    :param args: 文件中是否包含的字段
    :return: 包含args字段的文件
    '''
    s=os.path.abspath(s)
    if os.path.isdir(s): #目录
        for i in os.listdir(s):#遍历目录下的文件和目录，转换为绝对路径递归
            search(os.path.join(s,i),args)
    elif os.path.isfile(s): #文件
        s=os.path.split(s)#分离文件名和路径
        fielname=s[1]
        if args in fielname:
            print(os.path.join(s[0],s[1]))
    else:
        print ('请输入正确的路径')
search('.','e')