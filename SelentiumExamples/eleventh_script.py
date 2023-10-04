from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.select import Select
import time


try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/selects1.html")
    
    x_element = browser.find_element(By.CSS_SELECTOR, "#num1")
    tx = x_element.text    
    z_element = browser.find_element(By.CSS_SELECTOR, "#num2")
    tz = z_element.text    
    x = tx
    y = tz
    sum = (int(tx) + int(tz))
    print(sum)
    stroktype = str(sum)
    
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(stroktype)    
    
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)

finally:
    time.sleep(30)
    browser.quit()
