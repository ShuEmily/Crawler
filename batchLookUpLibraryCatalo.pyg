# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 10:19:40 2020
@author: sz215
"""


from selenium import webdriver #引入webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time #time模块
import pandas as pd
import numpy as np

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import csv
import os

t0= time.clock()
files_loc = 'C:/Users/sz215/.spyder-py3/duplicate_check/'
isbn_loc = 0
title_loc = 2
author_loc = 1

doc_list = os.listdir(files_loc)

def findthruISBN(isbn_loc, storage_mode):
    if(len(str(read_data[i].split('\t')[isbn_loc]))>=20):
        out_str.append('suspicious ISBN input, check input')
        return('not found')
    if(len(str(read_data[i].split('\t')[title_loc]))==0):
        exit
    else:
        url="https://library.duke.edu/"
        browser.get(url) #发送url请求
        browser.find_element_by_id("tab_books").click()
        searchISBN = read_data[i].split('\t')[isbn_loc]
        fieldElm = Select(browser.find_element_by_id('catalogcodeinput'))
        fieldElm.select_by_visible_text('Keywords')
        try:
            fieldElm.select_by_value('isbn_issn')
            keyword=browser.find_element_by_id("catalogqueryinput")#识别搜索框
            keyword.send_keys(str(searchISBN))#输入搜索内容
            keyword.send_keys(Keys.RETURN)
            if(storage_mode == 'online'):
                DKURes = browser.find_element_by_id('facet-access_type_f')
                DKURes.find_element_by_name('checkbox_access_type_f').click()
            elif(storage_mode == 'physical'):  
                DKURes = browser.find_element_by_id("facet-location_hierarchy_f")
                DKURes.find_element_by_link_text("Duke Kunshan Library").click()
                           
            tab1 = browser.find_element_by_xpath('.//section[@data-document-counter="'+str(0)+'"]')
            out_str.append('ISBN found')    
            return 'found'
        except:
            out_str.append('')
            return('not found')



def findthruISBN_backup(isbn_loc, storage_mode):
    if(len(str(read_data[i].split('\t')[isbn_loc]))>=20):
        out_str.append('suspicious ISBN input, check input')
        return('not found')
    if(len(str(read_data[i].split('\t')[title_loc]))==0):
        exit
    else:
        url="https://find.library.duke.edu/advanced"
        browser.get(url) #发送url请求
        time.sleep(0.05) #等待时间
        try:
            advsch = browser.find_element_by_id('advanced_search')
            isbn = advsch.find_element_by_id('isbn_issn')
            isbn.send_keys(read_data[i].split('\t')[isbn_loc])
        
            browser.find_element_by_class_name('advanced-search-submit').click()                      
            
            if(storage_mode == 'online'):
                DKURes = browser.find_element_by_id('facet-access_type_f')
                DKURes.find_element_by_name('checkbox_access_type_f').click()
            elif(storage_mode == 'physical'):
                DKURes = browser.find_element_by_id("facet-location_hierarchy_f")
                DKURes.find_element_by_link_text("Duke Kunshan Library").click()
                
            tab1 = browser.find_element_by_xpath('.//section[@data-document-counter="'+str(0)+'"]')
            tab1Link = tab1.find_element_by_xpath('.//a[@data-context-href]')   
            # out_str.append('potentially online found')
            temp_link = tab1Link.get_attribute('href')
            tab1Link.click()
            out_str.append('isbn found')
                # out_str.append(temp_link)
            return 'found'
        except:
            return('not found')
            exit
            # out_str.append('')
            # out_str.append('')





            
def findthruTitleAuthor(title_loc, author_loc, storage_mode):
    url="https://find.library.duke.edu/advanced"
    browser.get(url) #发送url请求
  
    try:
        advsch = browser.find_element_by_id('advanced_search')
        title = advsch.find_element_by_id('title')
        
        title.send_keys(read_data[i].split('\t')[title_loc].split("(")[0]) # .split(':')[0]
    
        author = advsch.find_element_by_id('author')
        author.send_keys(read_data[i].split('\t')[author_loc].split('-')[-1].split(',')[0].split(' ')[0])
        
        # browser.find_element_by_class_name('advanced-search-submit').click()                      
        
        try:
            browser.find_element_by_class_name('advanced-search-submit').click()                      
            browser.send_keys(Keys.RETURN)
        except:
            print(' ')
        
        if(storage_mode == 'online'):
           
            DKURes2 = browser.find_element_by_id('facet-access_type_f')
            DKURes2.find_element_by_name('checkbox_access_type_f').click()
        elif(storage_mode == 'physical'):
            
            DKURes2 = browser.find_element_by_id("facet-location_hierarchy_f")
            
            DKURes2.find_element_by_link_text("Duke Kunshan Library").click()
        
        
        time.sleep(0.05)
        tab1 = browser.find_element_by_xpath('.//section[@data-document-counter="'+str(0)+'"]')
        tab1Link = tab1.find_element_by_xpath('.//a[@data-context-href]')   
        # out_str.append('potentially online found')
        temp_link = tab1Link.get_attribute('href')
        tab1Link.click()
        
        detail = browser.find_element_by_id('other-details')
        # audio
        
        try:
            audio = detail.find_element_by_xpath('.//dd[@class="blacklight-physical_description_details_a"]').text
            if(audio == 'File type: audio file'):
                out_str.append('')
            else:
                out_str.append('title found')
                # out_str.append(temp_link)
            # tab1.find_element_by_xpath('.//a[@data-context-href]').click()
          # namep = browser.find_element_by_id('title-and-thumbnail')
        except:
            out_str.append('title found')    
        
    except:
        out_str.append('')
        
        
        
for ii in doc_list:
    browser = webdriver.Chrome(ChromeDriverManager().install())
    with open(files_loc+ii,encoding="utf8") as f:
         out_str = ['isbn','title','author','online_res','physical_res']
       # 'thru_isbn_online_res','thru_isbn_physical_res','online_thru_title','online_url','physical_thru_title','physical_url']
         with open(files_loc+ii[:-4]+'.csv','a') as fp:
                     wr = csv.writer(fp, dialect='excel',lineterminator='\n')
                     wr.writerow(out_str)
         fp.close() 
         
         read_data = f.readlines()
         for i in range(1,len(read_data)):#len(read_data)
             out_str = []
             out_str.append(read_data[i].split('\t')[isbn_loc]) # ISBN 
             out_str.append(read_data[i].split('\t')[title_loc])
             
             out_str.append(read_data[i].split('\t')[author_loc])
             if(findthruISBN_backup(isbn_loc, 'online') != 'found'):
                 findthruTitleAuthor(title_loc, author_loc, 'online')
               
             if(findthruISBN_backup(isbn_loc, 'physical') != 'found'): 
                 findthruTitleAuthor(title_loc, author_loc, 'physical')
             
             with open(files_loc+ii[:-4]+'.csv','a') as fp:
                 wr = csv.writer(fp, dialect='excel',lineterminator='\n')
                 wr.writerow(out_str)
                 fp.close()
                 f.close()    
               
browser.quit() #关闭所有与当前driver相关的窗口
browser.close() #关闭当前窗口
