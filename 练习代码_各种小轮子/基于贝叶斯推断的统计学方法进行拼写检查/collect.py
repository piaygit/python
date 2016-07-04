# -*-coding=utf-8 -*-
__author__ = 'piay'
'''
基于贝叶斯推断的统计学方法进行拼写检查
参考链接：http://www.ruanyifeng.com/blog/2012/10/spelling_corrector.html
'''

import re,collections

def words(text):
    '''
    定义words()函数，用来取出文本库的每一个词
    :param text:
    :return:
    '''
    return re.findall('[a-z]+',text.lower())

def train(features):
    '''
    定义一个train()函数，用来建立一个"字典"结构。
    文本库的每一个词，都是这个"字典"的键；它们所对应的值，就是这个词在文本库的出现频率
    :param features:
    :return:
    '''
    # 默认设定一个词的出现频率为1,没有在文本中出现，不代表没有这个单词
    model=collections.defaultdict(lambda:1)
    # 单词没出现一次，统计+一次
    for f in features:
        model[f]+=1
    return model

# 使用words()和train()函数,生成词频字典
NWORDS=train(words(file('big.txt').read()))

# 定义edits1()函数，用来生成所有与输入参数word的"编辑距离"为1的词。
alphabet='abcdefghijklmnopqrstuvwxyz'

def edits1(word):
    '''
    定义edits1()函数，用来生成所有与输入参数word的"编辑距离"为1的词。
    :param word:
    :return:
    '''

    # splits：将word依次按照每一位分割成前后两半。
    # 比如，'abc'会被分割成 [('', 'abc'), ('a', 'bc'), ('ab', 'c'), ('abc', '')] 。
    splits=[(word[:i],word[i:]) for i in range(len(word)+1)]

    # 依次删除word的每一位后、所形成的所有新词。比如，'abc'对应的deletes就是 ['bc', 'ac', 'ab'] 。
    deletes=[a+b[1:] for a,b in splits if b]

    # 依次交换word的邻近两位，所形成的所有新词。比如，'abc'对应的transposes就是 ['bac', 'acb'] 。
    transposes=[a+b[1]+b[0]+b[2:] for a,b in splits if len(b)>1]

    # 将word的每一位依次替换成其他25个字母，所形成的所有新词。比如，
    # 'abc'对应的replaces就是 ['abc', 'bbc', 'cbc', ... , 'abx', ' aby', 'abz' ] ，一共包含78个词（26 × 3）
    replaces=[a+c+b[1:] for a,b in splits for c in alphabet if b]

    # 在word的邻近两位之间依次插入一个字母，所形成的所有新词。比如，'abc'
    # 对应的inserts就是['aabc', 'babc', 'cabc', ..., 'abcx', 'abcy', 'abcz']，一共包含104个词（26 × 4）
    inserts=[a+c+b for a,b in splits for c in alphabet]

    # edit1()返回deletes、transposes、replaces、inserts的合集，
    # 这就是与word"编辑距离"等于1的所有词。对于一个n位的词，会返回54n+25个词。
    return set(deletes+transposes+replaces+inserts)

def edits2(word):
    '''
    定义edit2()函数，用来生成所有与word的"编辑距离"为2的词语
    进行两次deits1（word）操作
    :param word:
    :return:返回一个 (54n+25) * (54n+25) 的数组
    '''
    return set(e2 for e1 in edits1(word) for e2 in edits1(e1))

def known_edits2(word):
    '''
    edit2()改为known_edits2()函数，将返回的词限定为在文本库中出现过的词。
    :param word:
    :return:
    '''
    return set (e2 for e1 in edits1(word) for e2 in edits1(e1) if e2 in NWORDS)

def known(words):
    return set (w for w in words if w in NWORDS)

def correct(word):
    '''
    规则：
    1.如果word是文本库现有的词，说明该词拼写正确，直接返回这个词
    2.如果word不是现有的词，则返回"编辑距离"为1的词之中，在文本库出现频率最高的那个词；
    3.如果"编辑距离"为1的词，都不是文本库现有的词，则返回"编辑距离"为2的词中，出现频率最高的那个词；
    4.如果上述三条规则，都无法得到结果，则直接返回word。
    :param word:
    :return:
    '''
    candidatas=known([word]) or known(edits1(word)) or known_edits2(word) or [word]
    return max(candidatas,key=NWORDS.get)


print correct('speling')