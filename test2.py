#coding:utf-8
#@time     :     2018/7/9 20:23
#@Author     :    mengzh
#@file    :{name}.py
# @Site    : 
# @File    : test2.py
# @Software: PyCharm
from selenium import webdriver
import csv


url = "http://music.163.com/#/"

csv_file = open("playlist.csv", "w", newline=' ')
writer = csv.writer(csv_file)
writer.writerow(['标题', "播放数", "链接"])

while url != 'javascript:void(0)':
    driver = webdriver.PhantomJS()
    driver.get(url)

    driver.switch_to.frame("conentFrame")

    data = driver.find_element_by_id("m-plcontainer").\
        find_elements_by_tag_name("li")

    for i in range(len(data)):
        nb = data[i].find_element_by_class_name("nb").text
        if '万' in nb and int(nb.split("万")[0])>500:

            msk = data[i].find_element_by_css_selector("a.msk")

            writer.writerow([msk.get_attribute('title'),
                             nb, msk.get_attribute('href')])
    url = driver.find_element_by_css_selector("a.zbtn.znxt").\
        get_attribute('href')


csv_file.close()