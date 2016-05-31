#-*- coding=utf-8 -*-
class UrlManger(object):
    def __init__(self):
        self.new_urls=set()
        self.old_urls=set()
    def add_new_url(self,url):
        '''
        单个添加url
        :param url:单个url
        :return:
        '''
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:#不在未爬取和待爬取中
            self.new_urls.add(url)
    def add_new_urls(self,urls):
        '''
        多个url添加
        :param urls: url列表
        :return:
        '''
        if urls is None or len(urls)==0:
            return
        for url in urls:
            self.add_new_url(url)


    def has_new_url(self):
        '''

        :return: 带爬取不为空的时候返回,判断是否还有待爬取
        '''
        return len(self.new_urls)!=0

    def get_new_url(self):
        '''
        取出新的url，并从带爬取删除，加入已爬取
        :return:取出的待爬取url
        '''
        new_url=self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url


