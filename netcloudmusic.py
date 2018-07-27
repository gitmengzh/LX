#coding:utf-8
# @Time    : 2017/4/6 20:15
# @Author  : mengzh
# @File    : netcloudmusic.py
# @Software: PyCharm Community Edition

from Crypto.Cipher import AES
import base64
import requests
import json
import codecs
import time


#头部信息
headers = {
    'Host':"music.163.com",
    'Accept-Language':"en-US,en;q=0.8",
    'Accept-Encoding':"gzip, deflate, sdch",
    'Content-Type':"",
    'Cookie':"",
    'Connection':"",
    'Referer':""
}
#设置代理服务器

proxies = {
    'http':'http://121.232.146.184',
    'https':'https://144.255.48.197'
}
#offset的取值为（评论页数-1）*20，total第一页为true,其余页为false
first_param = '{rid:"",offset:"0",total:"true",limit:"20",csrf_toke:""}'#第一个参数
second_param = "010001" #第二个参数
thrid_param =