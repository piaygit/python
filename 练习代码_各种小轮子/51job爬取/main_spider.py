# -*-coding=utf-8 -*-
import html_parser


__author__ = 'piay'

class main_spider(object):

    def __init__(self):
        self.parser=html_parser.html_parser()



    def craw(self,url):
        self.parser.get_data(url)
        code=self.parser.code
        return code



q=main_spider()
for i in range(1,1000):
    url='http://search.51job.com/jobsearch/search_result.php?jobarea=090200%2C00&keyword=%E6%B5%8B%E8%AF%95&keywordtype=2&curr_page='+str(i)
    q.craw(url)
    if q.craw(url)!=200:
        break
