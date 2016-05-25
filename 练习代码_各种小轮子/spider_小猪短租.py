#coding=utf-8
import requests,re
from bs4 import BeautifulSoup

def get_page(url):
    html=requests.get(url)
    html.encoding='utf-8'
    return html.text
url='http://bj.xiaozhu.com/search-duanzufang-p1-0/'
page=get_page(url)
link_list=BeautifulSoup(page,"html5lib").find_all(href=re.compile(r'.*fangzi.*'))
link=[]
for i in link_list:
    link.append(i['href'])
print link




