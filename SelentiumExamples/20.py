from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    button = browser.find_element(By.ID, "book")
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    button.click()

    import math

    def calc(x):
      return str(math.log(abs(12*math.sin(int(x)))))

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    tx = x_element.text    
    x = int(tx)   
   
    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    y = calc(x) 
    input1.send_keys(y)    

    button = browser.find_element(By.CSS_SELECTOR, "#solve")
    button.click()
finally: 
    time.sleep(30)
    browser.quit()
