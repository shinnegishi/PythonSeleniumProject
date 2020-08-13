# -*- coding:utf-8 -*-
#AMAZON START

import sys
import os
import time
import re
import datetime
import keyboard
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
#import pandas
import time
from selenium.webdriver.chrome.options import Options
from pathlib import Path
import glob
import pandas as pd
from os.path import expanduser

PWD = os.getcwd()
HOME_DIR = expanduser("~")

RIYOUSYA_LIST_KEYWORD = "riyousha_list"
EXCEL_UPDATE_RIYOUSYA_INFO_ABSOLUTE_PATH = os.getcwd()+"\update_riyousya_info.xlsx"

#Update Riyousya File
COL_UPDATE_RIYOUSYA_LOGIN_ID = 0
COL_UPDATE_RIYOUSYA_BUSHO_CD = 1
COL_UPDATE_RIYOUSYA_BUSHO_NAME = 2
COL_UPDATE_RIYOUSYA_MAIL_ADDRESS = 3
COL_UPDATE_RIYOUSYA_LOCATION = 4

#Riyousya List
COL_RIYOUSYA_LIST_LOGIN_ID = 1
COL_RIYOUSYA_LIST_BUSHO_CD = 3
COL_RIYOUSYA_LIST_BUSHO_NAME = 4
COL_RIYOUSYA_LIST_MAIL_ADDRESS = 16
COL_RIYOUSYA_LIST_LOCATION = 6

LEAF_USER_NAME = "admin"
LEAF_USER_PASSWORD = "password15"

class CSVUpdater:

    def __init__(self):
        pass

    def update_csv(self,list_csv_path,update_excel_path=EXCEL_UPDATE_RIYOUSYA_INFO_ABSOLUTE_PATH):
        csvfile = pd.read_csv(list_csv_file)
        xlsxfile = pd.read_excel(update_excel_path)
        for i in range(0,len(xlsxfile)):
            xlsx_login_id = xlsxfile.iloc[i][COL_UPDATE_RIYOUSYA_LOGIN_ID]
            xlsx_busho_cd = xlsxfile.iloc[i][COL_UPDATE_RIYOUSYA_BUSHO_CD]
            xlsx_busho_name = xlsxfile.iloc[i][COL_UPDATE_RIYOUSYA_BUSHO_NAME]
            xlsx_mail_address = xlsxfile.iloc[i][COL_UPDATE_RIYOUSYA_MAIL_ADDRESS]
            xlsx_busho_location = xlsxfile.iloc[i][COL_UPDATE_RIYOUSYA_LOCATION]
            if xlsx_login_id is not None:
                for i2 in range(1,len(csvfile)):
                    if xlsx_login_id is csvfile.iloc[i2][COL_RIYOUSYA_LIST_LOGIN_ID]:
                        if xlsx_busho_cd is not None:
                            csvfile.iloc[i2][COL_RIYOUSYA_LIST_BUSHO_CD] = xlsx_busho_cd
                        if xlsx_busho_name is not None:
                            csvfile.iloc[i2][COL_RIYOUSYA_LIST_BUSHO_NAME] = xlsx_busho_name
                        if xlsx_busho_location is not None:
                            csvfile.iloc[i2][COL_RIYOUSYA_LIST_LOCATION] = xlsx_busho_location
                        if xlsx_mail_address is not None:
                            csvfile.iloc[i2][COL_RIYOUSYA_LIST_MAIL_ADDRESS] = xlsx_mail_address
        csvfile.to_csv(list_csv_path)

timestamp = datetime.datetime.now().strftime('%y%m%d%H%M')

#Headless Option
chrome_options = Options()
chrome_options.add_argument("--headless")

#Googleにアクセスして、タイトルをとってこれるかテスト
#browser = webdriver.Chrome(executable_path='/mnt/c/workspace/pydev/chromedriver.exe')
capabilities = DesiredCapabilities.CHROME
service = Service('./chromedriver.exe')
service.start()
browser = webdriver.Remote(service.service_url,capabilities)
#browser = webdriver.Remote(service.service_url,desired_capabilities=chrome_options.to_capabilities())
try:
    browser.get('https://rpatest.leaf-hrm.jp/')
    search_field = browser.find_element_by_xpath('//*[@id="inp_text"]')
    search_field.clear()
    search_field.send_keys(LEAF_USER_NAME)
    password_field = browser.find_element_by_xpath('//*[@name="data[Loginuser][password]"]')
    password_field.send_keys(LEAF_USER_PASSWORD)
    login_button = browser.find_element_by_xpath('//*[@id="btnLogin"]')
    login_button.click()#click login
    time.sleep(5)
    master_mentenance = browser.find_element_by_xpath("/html/body/div[1]/div/div[2]/ul/li[7]/a")
    master_mentenance.click()
    time.sleep(5)
    #利用者一括
    batch_user_upload = browser.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div[1]/div/div/div[1]/form/div[2]/a[2]")
    batch_user_upload.click()
    time.sleep(5)

    #利用者一括ファイル
    batch_user_update_file_button = browser.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div[1]/div/div/form/div[2]/table/tbody/tr/td[3]/button[2]")
    batch_user_update_file_button.click()
    time.sleep(5)

    #コピペ操作
    keyboard.press_and_release('wondows+e, ctrl+l, backspace')
    time.sleep(5)
    keyboard.write(HOME_DIR+"\Downloads")
    keyboard.press_and_release('enter')
    time.sleep(5)
    keyboard.press_and_release('tab')
    keyboard.write(RIYOUSYA_LIST_KEYWORD)
    keyboard.press_and_release('enter')
    time.sleep(5)
    keyboard.press_and_release('tab,tab')
    keyboard.press_and_release('ctrl+c')
    keyboard.press_and_release('ctrl+l, backspace')
    time.sleep(5)
    keyboard.write(PWD+"\work")
    keyboard.press_and_release('enter')
    keyboard.press_and_release('tab,tab')
    time.sleep(5)
    keyboard.press_and_release('ctrl+v')
    
    upload_csv_file_path = ''.join(glob.glob(os.getcwd()+"\work\*.csv"))
    csvu = CSVUpdater()
    csvu.update_csv(upload_csv_file_path)
    # Upload File
    browser.find_element_by_id("UserCsv").send_keys(upload_csv_file_path)
    batch_user_upload_file_button = browser.find_element_by_xpath('//*[@id="btnAdd"]')
    batch_user_upload_file_button.click()
    os.remove(upload_csv_file_path)



    #keyboard.press_and_release('shift+s, space')
    #keyboard.write('The quick brown fox jumps over the lazy dog.')

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