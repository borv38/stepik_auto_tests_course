from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import os 
import time


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")
  
    elements = browser.find_elements(By.CSS_SELECTOR, "input[type ='text']")
    for element in elements:
        element.send_keys("Мой ответ")  
        
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')  
    element = browser.find_element(By.CSS_SELECTOR, 'input[type="file"]')
    element.send_keys(file_path)
       
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()    
    
    time.sleep(1)

finally:
    time.sleep(30)
    browser.quit()
