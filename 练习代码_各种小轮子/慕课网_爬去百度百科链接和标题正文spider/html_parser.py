#-*- coding=utf-8 -*-
import re
import urlparse

from bs4 import BeautifulSoup


class HtmlParser(object):


    def _get_new_urls(self,page_url,soup):
        '''

        :param page_url: 页面url
        :param soup: 页面的soup解析数据
        :return:url列表
        '''
        new_urls=set()
        links=soup.find_all('a',href=re.compile(r'/view/\d{3,15}\.htm'))
        for link in links:
            new_url=link['href']
            #讲new_url按照page_url的格式组装
            new_full_url=urlparse.urljoin(page_url,new_url)
            new_urls.add(new_full_url)
        return new_urls




    def _get_new_data(self,page_url,soup):
        res_data={}
        res_data['url']=page_url
        title_node=soup.find("dd",class_="lemmaWgt-lemmaTitle-title").find('h1')
        res_data['title']=title_node.get_text()
        summary_node=soup.find('div',class_="lemma-summary")
        res_data['summary'] = summary_node.get_text()
        return res_data





    def parser(self,page_url,html_cont):
        if page_url is None or html_cont is None:
            return
        soup=BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')
        new_urls=self._get_new_urls(page_url,soup)
        new_data=self._get_new_data(page_url,soup)
        return new_urls,new_data