# -*- coding: UTF-8 -*- 

# In[1]:



from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import *
from selenium.webdriver import Chrome

import time

import json


# In[2]:


driver = webdriver.Chrome('./chromedriver')
driver.get('https://dcpc.nctu.edu.tw')


# In[3]:


# EDIT: student ID here or enter in the browser
inputUser = driver.find_element_by_name("txtAccount")
inputUser.send_keys('0410834')


# In[4]:


#EDIT: password here or enter in the browser
inputPwd = driver.find_element_by_name("txtPwd")
inputPwd.send_keys('PASSWORD')


# In[5]:



announces = []

# EDIT: total page of announcements
tot_page = 1

for page in range(0, tot_page):


    for course_id in ['03', '04', '05', '06', '07', '08', '09', '10', '11', '12']:

        lnkHistory = driver.find_element_by_id("ctl00_lnkHistory")
        lnkHistory.click()

        time.sleep(1)

        for i in range(0, page) :
            nextPage = driver.find_element_by_id("ctl00_ContentPlaceHolder1_DataNavigator1_ctl03")
            nextPage.click()
            time.sleep(1)

        try:
            course = driver.find_element_by_id("ctl00_ContentPlaceHolder1_dg_ctl"+course_id+"_lnbEnter")
            course.click()
        except NoSuchElementException:
            print(":P")
            continue

        time.sleep(2)

        announcements = driver.find_element_by_id("ctl00_lnkNewest")
        announcements.click()

        time.sleep(2)

        expire_announcements = driver.find_element_by_id("__tab_ctl00_ContentPlaceHolder1_tabAnnouncement_tpExpire")
        expire_announcements.click()

        time.sleep(2)

        title_list = driver.find_elements_by_class_name("bulletin_tfont")
        content_list = driver.find_elements_by_class_name("bulletin_lineheight")

        for i in range(len(title_list)):
            
            announces.append( {'title': title_list[i].text, 'content': "<br>".join(content_list[i].text.split("\n"))} )
            

            #print( json.dumps( {'title': title_list[i].text, 'content': "<br />".join(content_list[i].text.split("\n"))} ) )
            #writer.writerow({'title': title_list[i].text, 'content': content_list[i].text})


        lnkHome = driver.find_element_by_id("ctl00_btnHome")
        lnkHome.click()


# In[6]:


with open('an.json', 'w', encoding='utf8') as outfile:  
    json.dump(announces, outfile, ensure_ascii=False, indent=4)

