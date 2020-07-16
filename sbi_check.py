# -*- coding:utf-8 -*-

import sys
import os
import time
import re
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
#import pandas
import time
from selenium.webdriver.chrome.options import Options

timestamp = datetime.datetime.now().strftime('%y%m%d%H%M')

#Headless Option
chrome_options = Options()
chrome_options.add_argument("--headless")


#browser = webdriver.Chrome(executable_path='/mnt/c/workspace/pydev/chromedriver.exe')
capabilities = DesiredCapabilities.CHROME
service = Service('./chromedriver.exe')
service.start()
#browser = webdriver.Remote(service.service_url,capabilities)
browser = webdriver.Remote(service.service_url,desired_capabilities=chrome_options.to_capabilities())
username = raw_input("Username: ")
password = raw_input("Password: ")
try:
    browser.get('https://www.sbisec.co.jp/ETGate')
    username_field = browser.find_element_by_xpath('/html/body/table/tbody/tr[1]/td[2]/form/div/div/div/dl/dd[1]/div/input')
    username_field.clear()
    username_field.send_keys(username)
    password_field = browser.find_element_by_xpath("/html/body/table/tbody/tr[1]/td[2]/form/div/div/div/dl/dd[2]/div/input")
    password_field.send_keys(password)
    login_button = browser.find_element_by_xpath("/html/body/table/tbody/tr[1]/td[2]/form/div/div/div/p[2]/a/input")
    login_button.click()#click login
    time.sleep(5)
    account_management = browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/ul/li[3]/a/img")
    account_management.click()
    time.sleep(3)
    account_balance = browser.find_element_by_xpath("/html/body/div[1]/table/tbody/tr/td[1]/table/tbody/tr[2]/td/table[1]/tbody/tr/td/form/table[2]/tbody/tr[1]/td[2]/table[5]/tbody/tr/td[1]/table[4]/tbody/tr[8]/td[2]/div/b").text
    print("Current Account Balance: {}".format(account_balance))

    """
    with open('amazon_%s.txt'%(timestamp), 'w') as f:
        while True: #continue until getting the last page
            books = browser.find_elements_by_css_selector('li.zg-item-immersion')
            book_list = []
            for book in books:
                book_title = book.find_element_by_css_selector('div.p13n-sc-truncated').get_attribute("title").encode('utf-8').strip('\n')
                if book_title in book_list:
                    pass
                else:
                    if(len(book_title) > 0):
                        book_list.append(book_title)
            f.write("\n".join(book_list))

            #time.sleep(20) # Let the user actually see something!
            #browser.quit()
            #page+=1
            if len(browser.find_elements_by_css_selector('li.a-last a')) > 0:
                next_url = browser.find_element_by_css_selector('li.a-last a').get_attribute("href")
                browser.get(next_url)
            else:
                time.sleep(1)
                browser.quit()
    """
except Exception as e:
    print(e.message)