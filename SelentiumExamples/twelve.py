from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.select import Select
import time


try:

    from selenium import webdriver
    browser = webdriver.Chrome()
    browser.execute_script("document.title='Script executing';alert('Robots at work');")

    time.sleep(1)

finally:
    time.sleep(30)
    browser.quit()
