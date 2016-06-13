# -*-coding=utf-8 -*-


from qsbk_spider import html_parser, insert_mysql

__author__ = 'piay'


class main_spider(object):
    def __init__(self):
        self.parser = html_parser.html_parser()
        self.insert_data = insert_mysql.insert_mysql()


    def craw(self, url):
        page_data = self.parser.HtmlParser(url)
        self.insert_data.insert_mysql(page_data)


if __name__ == '__main__':
    for page in range(1,100):
        url = 'http://www.qiushibaike.com/hot/page/' + str(page)
        spider = main_spider()
        m = spider.craw(url)





