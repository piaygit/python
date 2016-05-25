#coding=utf-8
import requests,re
from bs4 import BeautifulSoup
url='http://bj.xiaozhu.com/search-duanzufang-p1-0/'
html=requests.get(url)
html.encoding = 'utf-8'
page=html.text
page=re.search('id="page_list"(.*?)class="result_foot clearfix"', page, re.S).group()
soup=BeautifulSoup(page, "html5lib")
soup=soup.find_all("a")
m=re.compile(r'[a-zA-z]+://[^\s]*')
last_link=[]
for i in soup:
    link=re.findall(m, str(i))
    if len(link) == 2: # 得到最后类似内容：http://www.xiaozhu.com/fangdong/10791900/"
        p_link=link[0]
        new_link=p_link[:len(p_link)-1] # 去掉最后一个"号字符
        if 'fangzi' in new_link:# 去除房东的链接
            last_link.append(new_link)
print last_link


