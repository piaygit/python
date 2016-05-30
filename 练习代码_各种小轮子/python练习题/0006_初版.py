#-*- coding=utf-8 -*-
'''
你有一个目录，放了你一个月的日记，都是 txt，为了
避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词。
'''
from collections import Counter
words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]

count=Counter(words)#统计每个单词出现的次数
print count
#Counter({'eyes': 8, 'the': 5, 'look': 4, 'into': 3, 'my': 3, 'around': 2, "you're": 1, "don't": 1, 'under': 1, 'not': 1})
count_most=count.most_common(3) #统计出现次数最多的三个
print count_most
#[('eyes', 8), ('the', 5), ('look', 4)]
