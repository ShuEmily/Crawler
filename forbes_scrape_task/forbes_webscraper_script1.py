# -*- coding: utf-8 -*-
"""
Created on OCT 26 10:19:40 2021
@author: sz
"""

from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time 
import pandas as pd
import numpy as np
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import csv
import os
import pyperclip
from datetime import date, timedelta



options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

browser = webdriver.Chrome(executable_path=r"C:\Users\37251\libraryCatalogCheck\chromedriver.exe",  options=options) 
url="https://www.forbes.com/business/"
browser.get(url) # send url request

# ######################
# # signing in the web #
# ######################
browser.find_element_by_class_name("login--wrapper").click()
time.sleep(3)

# change the control to signin page       
iframe_0 = browser.find_elements_by_tag_name('iframe')
browser.switch_to.frame(iframe_0[-1])
time.sleep(10)

# fill in acct info 
id = browser.find_element_by_id('email')
id.send_keys('372514275@qq.com')
pswd = browser.find_element_by_id('password')
pswd.send_keys('12341234ZEze2@')
pswd.send_keys(Keys.RETURN)
time.sleep(2)

######################
#  Store all links   #
######################
browser.switch_to.default_content()
time.sleep(3)

lists = browser.find_elements_by_tag_name("a") # get all href links on the website
links = [] # Empty list for storing links

yst_day = date.today() - timedelta(days=1)  # get yesterday's data
d1 = yst_day.strftime("%Y/%m/%d/") # format yesterday's date

# use today's article links
for lis in lists:
    try:
        temp_link = lis.get_attribute('href')
        # if('2021/10/26/' in temp_link):
        if(d1 in temp_link):
        # Fetch and store the links
            links.append(temp_link)
    except:
        continue

links = set(links) # make sure the stored link lists are unique

######################
#    Extract Text    #
######################
# Loop through all the links and launch one by one
for link in links:
    browser.get(link)
    # Scraping the text
    try:
        element=browser.find_element_by_tag_name('body')
        temp_link_name = link.split('/')[-2]
        # write to file
        file_object = open(r"C:/Users/37251/Desktop/2021Fall/forbes3/" + temp_link_name+'.txt','w')
        file_object.write(element.text)
        file_object.close()
    except:
        continue
    time.sleep(6)

browser.quit()

# Below are links showing ads, which caused interruption in text scraping. I did not process since the procedure is similar to sign in handling demonstrated above.
# further_links = ['https://www.forbes.com/sites/katedingwall/2021/10/26/backcountry-and-beaujolais-patagonia-now-sells-natural-wine/',
# 'https://www.forbes.com/sites/danidiplacido/2021/10/26/dune-review-the-cinema-strikes-back/',
# 'https://www.forbes.com/sites/manuelveth/2021/10/26/more-than-a-plan-b-wolfsburg-hire-former-werder-boss-florian-kohfeldt-1/'
# 'https://www.forbes.com/sites/kimwesterman/2021/10/26/sound-bath-of-luxurious-silence-at-chteau-du-sureau/'
# ]


