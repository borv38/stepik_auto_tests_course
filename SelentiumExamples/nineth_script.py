from selenium import webdriver
from selenium.webdriver.common.by import By
import time


try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/math.html")
    
    import math
    
    def calc(x):
      return str(math.log(abs(12*math.sin(int(x)))))
    
    x_element = browser.find_element(By.CSS_SELECTOR, "span#input_value.nowrap")
    x = x_element.text

    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    y = calc(x)
    input1.send_keys(y)
 
    option1 = browser.find_element(By.CSS_SELECTOR, '[for="robotCheckbox"]')
    option1.click()

    option1 = browser.find_element(By.CSS_SELECTOR, '[for="robotsRule"]')
    option1.click()

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
