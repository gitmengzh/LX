#coding:utf-8
#@time     :     2018/8/15 19:20
#@Author     :    mengzh
#@file    :{name}.py
# @Site    : 
# @File    : spider for ti8.py
# @Software: PyCharm



from selenium import webdriver
import csv


base_url = "https://www.dota2.com.cn/international/2018/match"
data = ["?date=2018-08-16","?date=2018-08-17","?date=2018-08-18","?date=2018-08-19","?date=2018-08-21","?date=2018-08-22","?date=2018-08-23","?date=2018-08-24","?date=2018-08-25","?date=2018-08-26",]

#csv_file = open("playlist.csv", "w", newline=' ')
#writer = csv.writer(csv_file)
#writer.writerow(['标题', "播放数", "链接"])

#while url != 'javascript:void(0)':
i = 0
url = base_url+data[i]
driver = webdriver.PhantomJS()
if i ==0:
    driver.get(url)
    driver.maximize_window()
    driver.find_element_by_xpath("/html/body/div[2]/div[3]/div[2]/div[2]/a[1]").click()

    #round = driver.find_element_by_xpath("")
    team1 = driver.find_element_by_xpath("/html/body/div[2]/div[3]/div[2]/div[3]/div[1]/ul/li[1]/div[2]/div[1]/div/span[1]").text()
    team2 = driver.find_element_by_xpath("/html/body/div[2]/div[3]/div[2]/div[3]/div[1]/ul/li[1]/div[2]/div[1]/div/span[2]").text()
    print (team1+'vs'+team2)

    '''data = driver.find_element_by_id("m-plcontainer").\
        find_elements_by_tag_name("li")

for i in range(len(data)):
    nb = data[i].find_element_by_class_name("nb").text
    if '万' in nb and int(nb.split("万")[0])>500:

        msk = data[i].find_element_by_css_selector("a.msk")

        writer.writerow([msk.get_attribute('title'),
                             nb, msk.get_attribute('href')])
url = driver.find_element_by_css_selector("a.zbtn.znxt").\
        get_attribute('href')


#csv_file.close()'''