#-*- coding=utf-8 -*-
import urllib2


class HtmlDownloader(object):
    '''
    返回下载器的内容
    '''
    def download(self,url):
        if url is None:
            return None
        response = urllib2.urlopen(url)
        if response.getcode()!=200:
            return None
        return response.read()




