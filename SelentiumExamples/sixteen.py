from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/alert_accept.html")
    button = browser.find_element(By.TAG_NAME, "button")
    button.click() 
    confirm = browser.switch_to.alert
    confirm.accept()
    
    
    import math

    def calc(x):
      return str(math.log(abs(12*math.sin(int(x)))))
     
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    tx = x_element.text    
    x = int(tx)    
 
    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    y = calc(x) 
    input1.send_keys(y)
     
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()    
    
    time.sleep(1)

finally:
    time.sleep(30)
    browser.quit()
