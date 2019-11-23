from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from bs4 import BeautifulSoup
import re
import pandas as pd
import os


"""
py virtual display stuff

from pyvirtualdisplay import Display
from selenium import webdriver

display = Display(visible=0, size=(1024, 768))
display.start()
"""
#usernameStr = 'tanishq.nalloju@gmail.com'
#passwordStr = 'venkata009'

browser = webdriver.Chrome(r'C:\Users\tanis\Downloads\chromedriver.exe')
browser.get(('https://www.kluniversity.in/flist.aspx'))

#LoginButton = browser.find_element_by_id('')

# fill in username and hit the next button
#username = browser.find_element_by_id('login-email')
#username.send_keys(usernameStr)
"""
WebDriverWait(browser, 10)
password  = browser.find_element_by_name('login-password')
password.send_keys(passwordStr)

"""
"""
password = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.ID, 'login-password')))
password.send_keys(passwordStr)


signInButton = browser.find_element_by_id('login-submit')
signInButton.click()
"""

#browser.close()

"""
page return and display

print (browser.page_source)


display.stop()
"""