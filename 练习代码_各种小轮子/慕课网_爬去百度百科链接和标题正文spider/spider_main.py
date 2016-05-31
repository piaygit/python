#-*- coding=utf-8 -*-
from spider import url_manager, html_downloader, html_parser, html_output


class Spidermain(object):
    def __init__(self):
        self.urls=url_manager.UrlManger() #初始化url管理器
        self.downloader=html_downloader.HtmlDownloader()#初始化url下载器
        self.parser=html_parser.HtmlParser()#初始化html解析器
        self.outputer=html_output.HtmlOutputer()#初始化html输出器


    def craw(self,root_url):
        count=1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():  #判断是否还有为爬取的url
            try:
                new_url=self.urls.get_new_url()#取出待爬取的url
                print 'craw %d:%s'%(count,new_url)
                html_cont=self.downloader.download(new_url) #下载页面
                new_urls,new_data=self.parser.parser(new_url,html_cont) #获取页面的url和data
                self.urls.add_new_urls(new_urls) #将页面的新的url添加到列表中
                self.outputer.collect_data(new_data) # 收集数据
                if count==100:
                    break
                count=count+1
            except:
                print "craw error:%s",new_url
        self.outputer.output_html()#输入数据







if __name__=='__main__':
    root_url='http://baike.baidu.com/item/%E9%9C%B9%E9%9B%B3%E5%B8%83%E8%A2%8B%E6%88%8F'
    #创建一个spider
    obj_spider=Spidermain()
    #调用url启动爬虫
    obj_spider.craw(root_url)


