# -*-coding:utf-8-*-
import os  
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.chrome.options import Options

#Headless Option
chrome_options = Options()  
chrome_options.add_argument("--headless")  

#driver = webdriver.Chrome(executable_path='C:/path/to/chromedriver.exe')
capabilities = DesiredCapabilities.CHROME
service = Service('/Users/suc806/Project/Python/chromium_project/chromedriver.exe')
service.start()
driver = webdriver.Remote(service.service_url,desired_capabilities=chrome_options.to_capabilities())
#driver = webdriver.Remote(service.service_url,capabilities)
driver.get('http://www.yahoo.co.jp/');
time.sleep(5) # Let the user actually see something!
driver.quit()


"""
import os  
from selenium import webdriver  
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.chrome.options import Options

service = webdriver.chrome.service.Service(os.path.abspath(Ågchromedriver"))  
service.start()

chrome_options = Options()  
chrome_options.add_argument("--headless")  

# path to the binary of Chrome Canary that we installed earlier  
chrome_options.binary_location = '/Applications/Google Chrome   Canary.app/Contents/MacOS/Google Chrome Canary'

driver = webdriver.Remote(service.service_url,   desired_capabilities=chrome_options.to_capabilities())
"""

"""
import os  
from selenium import webdriver  
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.chrome.options import Options  

chrome_options = Options()  
chrome_options.add_argument("--headless")  
chrome_options.binary_location = '/Applications/Google Chrome   Canary.app/Contents/MacOS/Google Chrome Canary'`    

driver = webdriver.Chrome(executable_path=os.path.abspath(Ågchromedriver"),   chrome_options=chrome_options)  
driver.get("http://www.duo.com")`  

magnifying_glass = driver.find_element_by_id("js-open-icon")  
if magnifying_glass.is_displayed():  
  magnifying_glass.click()  
else:  
  menu_button = driver.find_element_by_css_selector(".menu-trigger.local")  
  menu_button.click()`  

search_field = driver.find_element_by_id("site-search")  
search_field.clear()  
search_field.send_keys("Olabode")  
search_field.send_keys(Keys.RETURN)  
assert "Looking Back at Android Security in 2016" in driver.page_source   driver.close()` 
"""