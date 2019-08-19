# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 21:45:44 2019

@author: liubinbin
"""

u1 = 'https://movie.douban.com/subject/26584183/photos?type=S&start=0&sortby=like&size=a&subtype=a'

urllst = []
for i in [0, 30, 60, 90]:
    # 格式化字符串
    urllst.append('https://movie.douban.com/subject/26584183/photos?type=S&start=%i&sortby=like&size=a&subtype=a' % i)



import requests
from bs4 import BeautifulSoup

r = requests.get(url = u1)
soup = BeautifulSoup(r.text, 'lxml')

div = soup.find('div', class_="nav-items")
ul = div.find('ul')
li = ul.find_all('li')


url1 = 'https://movie.douban.com/subject/26584183/photos?type=S&start=90&sortby=like&size=a&subtype=a'

r = requests.get(url = url1)
soup = BeautifulSoup(r.text, 'lxml')

div = soup.find('div', class_="article")
ul = div.find('ul')
lis = ul.find_all('li')

li1 = lis[0]
img = li1.find('img')
pic_url = img['src']

photos_urls = []
for i in lis:
    img = i.find('img')
    photos_urls.append(img['src'])

photo = photos_urls[0]

import os
os.chdir('E:/data_analysis/pic/')

imgr = requests.get(url = photo)

with open('p1.jpg', 'wb') as f:
    # 通过write方法将二进制数据写入file对象对应的文件夹中
    f.write(imgr.content)

n = 1
for i in photos_urls:
    # print(i)
    pic_name = i.split('/')[-1]
    # print(pic_name)
    img_r = requests.get(url = i)
    with open(pic_name, 'wb') as f:
    # 通过write方法将二进制数据写入file对象对应的文件夹中
        f.write(img_r.content)
    print('成功获取%i张图片' % n)
    n += 1










