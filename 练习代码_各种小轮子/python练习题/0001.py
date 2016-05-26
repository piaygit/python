#-*- coding=utf-8 -*-
'''
做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），
使用 Python 如何生成 200 个激活码（或者优惠券）？
'''
import uuid,random

#方法1,通过uuid1得到随机数
def creat_code(number=200):
    '''

    :param number: 生成激活码个数，默认200个
    :return: code_list 返回激活码的列表
    '''
    code_list=[]
    for i in range(number):
        code=uuid.uuid1()#7ac14f61-234a-11e6-9215-047d7b18f39f 得到类似的格式
        code=str(code).replace('-','')
        code_list.append(code)
    return code_list

#方法二 通过随机数得到
def creat_code_forrandom(len_number=8,number=200):
    '''

    :param len_number:激活码位数
    :param number:激活码个数
    :return:
    '''
    code_list=[]
    for i in range(number):
        str_code=random.sample('zyxwvutsrqponmlkjihgfedcba',len_number/2) #生成一半字符
        str_code=''.join(str_code)#list转换为str
        num=len_number-len_number/2
        number_code=random.randint(num*100,num*1000-1)#剩下一般生成数字
        code=str_code+str(number_code)
        code_list.append(code)
    return code_list
print creat_code()
print creat_code_forrandom()