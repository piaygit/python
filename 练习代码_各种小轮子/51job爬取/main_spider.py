# -*-coding=utf-8 -*-
import html_parser


__author__ = 'piay'

class main_spider(object):

    def __init__(self):
        self.parser=html_parser.html_parser()



    def craw(self,url):
        self.parser.get_data(url)

    def get_next_url(self,url):
        next_page_url=self.parser.get_next_page(url)
        return next_page_url



# q=main_spider()
# for i in range(1,1000):
#     url='http://search.51job.com/jobsearch/search_result.php?jobarea=090200%2C00&keyword=%E6%B5%8B%E8%AF%95&keywordtype=2&curr_page='+str(i)
#     q.craw(url)
#     if q.craw(url)!=200:
#         break

if __name__=='__main__':
    spider_server=main_spider()
    url = 'http://search.51job.com/jobsearch/search_result.php?jobarea=090200%2C00&keyword=%E6%B5%8B%E8%AF%95&keywordtype=2&curr_page=1'
    next_page_url=url
    while next_page_url:
        # 插入数据
        spider_server.craw(next_page_url)
        # 得到下一页的链接
        next_page_url=spider_server.get_next_url(next_page_url)




