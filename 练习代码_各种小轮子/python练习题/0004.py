#coding=utf-8
'''
任一个英文的纯文本文件，统计其中的单词出现的个数。
'''

def serach_word(path,word,issize=0):
    '''

    :param path: 文件路径
    :param word: 搜索的单词
    :param issize: 是否区分大小写，默认区分，其他参数表示不区分
    :return:num 返回数量
    '''
    num=0
    try:
        with open(path) as f:
            for line in f:
                if issize == 0:  # 区分大小写
                    if word in line:
                        num+=1
                else:  # 不区分大小写
                    line=(str(line)).lower()
                    word=word.lower()
                    if word in line:
                        num+=1
    except:
        print('请检查文件或路径是否正确')
    return num
m=serach_word('./0004_文本','china',4)
print m