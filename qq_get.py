# -*- coding: utf-8 -*-

# 爬取sougou音乐的爬虫
# author: zyy

import requests
from lxml import etree
from selenium import webdriver
import time
import codecs


url = 'http://mp3.sogou.com/top/tag_list.html'
lxml = requests.get(url).content
selector = etree.HTML(lxml)
tags = selector.xpath("//div[@id='tag_sort_03']/ul")
driver = webdriver.Chrome()
driver.maximize_window()
f = codecs.open("x.txt", 'a+', 'utf-8')
print tags
for tag in tags:
    music_type = tag.xpath('li/a/text()')
    music_href = tag.xpath("li/a[@href]")
    print music_type
i = 0
while(i<len(music_type)):
    now_type = music_type[i]
    if(i == 0):
        go_href = "http://mp3.sogou.com/" + music_href[i].get('href')
        driver.get(go_href)
        print go_href
        j = 0 
        for j in range(60):
            if(j >= 30):
                in_lxml = driver.page_source
                songs = etree.HTML(in_lxml).xpath("//ul[@id='tag_ul']/li")
                k = 0
                for k in range(len(songs)):
                    x = songs[k].get('param').split(',')
                    num = 0
                    for num in range(len(x)):
                        if(num == 2 or num == 3 or num == 5):
                            f.write(x[num])
                            f.write('|')
                    f.write(now_type +'\n')
            driver.execute_script("window.scrollBy(0,10000)")
            time.sleep(3)
            elem = driver.find_element_by_xpath("//div[@id='tag_page_div']/a[@class='pager_btn next']")
            if(elem == -1):
                break
            elem.click()
    i = i + 1
    # for m_type in 
# parsehtmlMusicList(url)