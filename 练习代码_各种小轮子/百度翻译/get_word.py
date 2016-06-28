# -*-coding=utf-8 -*-



__author__ = 'piay'
class get_word(object):

    def getword(self):
        '''
        获取需要翻译的单词，
        :return:返回urlencode后的翻译单词
        '''
        query=raw_input('请输入需要翻译的单词：')
        # query=urllib.quote(query)
        return query


