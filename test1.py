#coding:utf-8
#@time     :     2018/7/9 20:02
#@Author     :    mengzh
#@file    :{name}.py
# @Site    : 
# @File    : test1.py
# @Software: PyCharm

from urllib2 import urlopen
from bs4 import BeautifulSoup
html = urlopen('http://jr.jd.com')
bs_obj = BeautifulSoup(html.read(),'html.parser')
text_list = bs_obj.find_all("a","nav-item-primary")
for text in text_list:
    print(text.get_text())

html.close()