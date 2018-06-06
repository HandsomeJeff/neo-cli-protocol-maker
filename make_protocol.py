#!/usr/bin/env python
# -*- encoding: utf8 -*-

import re

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup, SoupStrainer
from make_json import writeToJSON

try:
    driver = webdriver.Chrome()
except:
    driver = webdriver.Firefox()
url = "http://monitor.cityofzion.io/"


driver.get(url)

html = driver.page_source


soup = BeautifulSoup(html, "lxml")

table = str(soup.findAll('tr', {'class':'color-success'})).decode('utf-8')
alist = table.encode('utf-8').split('tr')

seedlist = []

for a in alist:
    searchUrl = re.search(r'http(.*)binding">(.*?):10332', a, re.M|re.I)
    if searchUrl:
        if len(seedlist) < 5:
            seedlist.append(searchUrl.group(2)+':10333')
        else:
            break

writeToJSON(seedlist)

print "end>>>>>>>>>>>>>"
