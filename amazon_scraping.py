# -*-coding:utf-8-*-

"""
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
service = Service('./chromedriver.exe')
service.start()
#driver = webdriver.Remote(service.service_url,desired_capabilities=chrome_options.to_capabilities())
driver = webdriver.Remote(service.service_url,capabilities)
#driver.get('http://www.yahoo.co.jp/');
driver.get('https://www.amazon.co.jp/gp/bestsellers/books/466282');
time.sleep(20) # Let the user actually see something!
driver.quit()
"""


"""
#AMAZON START

mport sys
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import pandas
import time

#Googleにアクセスして、タイトルをとってこれるかテスト
#browser = webdriver.Chrome(executable_path='/mnt/c/workspace/pydev/chromedriver.exe')
capabilities = DesiredCapabilities.CHROME
service = Service('./chromedriver.exe')
service.start()
browser = webdriver.Remote(service.service_url,capabilities)

#1

#args = sys.argv
df = pandas.read_csv('amazon_list.csv', index_col=0)

#2

query = args[1]

#3

browser.get('https://www.amazon.co.jp/gp/bestsellers/books/466282')

#4

#page = 1

#5

while True: #continue until getting the last page
    books = browser.find_elements_by_css_selector('li.zg-item-immersion')

    for book in books:
        book_title = book.find_elements_by_css_selector('div.p13n-sc-truncated()').text
        print(book_title)


    #5-1

    """
    if len(browser.find_elements_by_css_selector("li.pager-next .pager-cell:nth-child(1) a")) > 0:
        print("######################page: {} ########################".format(page))
        print("Starting to get posts...")

        #5-1-2

        posts = browser.find_elements_by_css_selector(".items-box")

        #5-1-3

        for post in posts:
            title = post.find_element_by_css_selector("h3.items-box-name").text

            #5-1-3-1

            price = post.find_element_by_css_selector(".items-box-price").text
            price = price.replace('¥', '')

            #5-1-3-2

            sold = 0
            if len(post.find_elements_by_css_selector(".item-sold-out-badge")) > 0:
                sold = 1

            url = post.find_element_by_css_selector("a").get_attribute("href")
            se = pandas.Series([title, price, sold,url],['title','price','sold','url'])
            df = df.append(se, ignore_index=True)

        #5-1-4

        page+=1

        btn = browser.find_element_by_css_selector("li.pager-next .pager-cell:nth-child(1) a").get_attribute("href")
        print("next url:{}".format(btn))
        browser.get(btn)
        print("Moving to next page......")

    #5-2

    else:
        print("no pager exist anymore")
        break
    """
#6
df.to_csv("{}.csv".format(query))
print("DONE")


#AMAZON END
"""


"""
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

service = webdriver.chrome.service.Service(os.path.abspath(�gchromedriver"))
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

driver = webdriver.Chrome(executable_path=os.path.abspath(�gchromedriver"),   chrome_options=chrome_options)
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
