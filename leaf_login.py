# -*- coding:utf-8 -*-

import sys
import os
import time
import re
import datetime
import keyboard
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

import time
from selenium.webdriver.chrome.options import Options

import glob
import pandas as pd
from os.path import expanduser

PWD = os.getcwd()
HOME_DIR = expanduser("~")

RIYOUSYA_LIST_KEYWORD = "riyousya_list"
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

    def update_csv(self,upload_csv_file_path,update_excel_path=EXCEL_UPDATE_RIYOUSYA_INFO_ABSOLUTE_PATH):
        riyousya_csv_df = pd.read_csv(upload_csv_file_path,encoding="sjis")
        xlsxfile = pd.read_excel(update_excel_path)
        for i in range(0,len(xlsxfile)):
            xlsx_login_id = xlsxfile.iloc[i][COL_UPDATE_RIYOUSYA_LOGIN_ID]
            xlsx_busho_cd = xlsxfile.iloc[i][COL_UPDATE_RIYOUSYA_BUSHO_CD]
            xlsx_busho_name = xlsxfile.iloc[i][COL_UPDATE_RIYOUSYA_BUSHO_NAME]
            xlsx_mail_address = xlsxfile.iloc[i][COL_UPDATE_RIYOUSYA_MAIL_ADDRESS]
            xlsx_busho_location = xlsxfile.iloc[i][COL_UPDATE_RIYOUSYA_LOCATION]
            if xlsx_login_id is not None:
                for i2 in range(1,len(riyousya_csv_df)):
                    csv_login_id = riyousya_csv_df.iloc[i2][COL_RIYOUSYA_LIST_LOGIN_ID]
                    if xlsx_login_id == csv_login_id:                       
                        if xlsx_busho_cd is not None:
                            riyousya_csv_df.iloc[i2][COL_RIYOUSYA_LIST_BUSHO_CD] = xlsx_busho_cd
                        if xlsx_busho_name is not None:
                            riyousya_csv_df.iloc[i2][COL_RIYOUSYA_LIST_BUSHO_NAME] = xlsx_busho_name
                        if xlsx_busho_location is not None:
                            riyousya_csv_df.iloc[i2][COL_RIYOUSYA_LIST_LOCATION] = xlsx_busho_location
                        if xlsx_mail_address is not None:
                            riyousya_csv_df.iloc[i2][COL_RIYOUSYA_LIST_MAIL_ADDRESS] = xlsx_mail_address

        timestamp = datetime.datetime.now().strftime('%y%m%d%H%M')
        upload_csv_work_file_path = "{cwd}\work\{csvprefix}{timestamp}.csv".format(cwd=os.getcwd(),csvprefix="upload_",timestamp=timestamp)
        try:
            riyousya_csv_df.to_csv(upload_csv_work_file_path,encoding="sjis",index=False)
        except Exception as e:
            print(e.message())
        return upload_csv_work_file_path

        

class KeyboardShortcut:
    def __init__(self):
        pass

    def copy_and_paste_list_file(self):
        #コピペ操作
        keyboard.press_and_release('windows+e')
        time.sleep(5)
        keyboard.press_and_release('ctrl+l, backspace')
        time.sleep(5)
        keyboard.write(HOME_DIR+"\Downloads")
        keyboard.press_and_release('enter')
        time.sleep(5)
        keyboard.press_and_release('ctrl+l')
        keyboard.press_and_release('tab')
        time.sleep(5)
        keyboard.write(RIYOUSYA_LIST_KEYWORD)
        time.sleep(5)
        keyboard.press_and_release('enter')
        time.sleep(3)
        keyboard.press_and_release('tab')
        time.sleep(3)
        keyboard.press_and_release('tab')
        time.sleep(3)
        keyboard.press_and_release('down,up')

        #利用者一括ファイルのコピー
        keyboard.press_and_release('ctrl+c')
        keyboard.press_and_release('ctrl+l, backspace')
        time.sleep(5)
        keyboard.write(PWD+"\work")
        keyboard.press_and_release('enter')
        time.sleep(5)
        keyboard.press_and_release('ctrl+l')
        time.sleep(5)
        keyboard.press_and_release('tab')
        time.sleep(3)
        keyboard.press_and_release('tab')
        time.sleep(3)
        keyboard.press_and_release('tab')
        time.sleep(3)
        keyboard.press_and_release('ctrl+v')

#Headless Option
chrome_options = Options()
chrome_options.add_argument("--headless")

#Googleにアクセスして、タイトルをとってこれるかテスト
#browser = webdriver.Chrome(executable_path='/mnt/c/workspace/pydev/chromedriver.exe')
capabilities = DesiredCapabilities.CHROME
service = Service('./chromedriver.exe')
service.start()
browser = webdriver.Remote(service.service_url,capabilities)
#Headless Option
#browser = webdriver.Remote(service.service_url,desired_capabilities=chrome_options.to_capabilities())

try:
    # login
    browser.get('https://rpatest.leaf-hrm.jp/')
    search_field = browser.find_element_by_xpath('//*[@id="inp_text"]')
    search_field.clear()
    search_field.send_keys(LEAF_USER_NAME)
    password_field = browser.find_element_by_xpath('//*[@name="data[Loginuser][password]"]')
    password_field.send_keys(LEAF_USER_PASSWORD)
    login_button = browser.find_element_by_xpath('//*[@id="btnLogin"]')
    login_button.click()#click login
    time.sleep(5)
    
    #マスタメンテナンス
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

    csvfiles = glob.glob(HOME_DIR+"\Downloads\*.csv")
    csvfiles.sort(key=os.path.getmtime)
    upload_csv_file_path = csvfiles[-1]

    # Update CSV Records
    csvu = CSVUpdater()
    upload_csv_work_file_path = csvu.update_csv(upload_csv_file_path)
    time.sleep(15)

    # Upload File
    browser.find_element_by_id("UserCsv").send_keys(upload_csv_work_file_path)
    batch_user_upload_file_button = browser.find_element_by_xpath('//*[@id="btnAdd"]')
    batch_user_upload_file_button.click()
    time.sleep(4)
    keyboard.press_and_release('tab,tab,enter')
    time.sleep(15)
    browser.close()
    os.remove(upload_csv_file_path)
    os.remove(upload_csv_work_file_path)

except Exception as e:
    print("######## Exception ########")
    print(e.message)