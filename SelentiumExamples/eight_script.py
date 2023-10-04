from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/registration2.html")

    input1 = browser.find_element(By.CSS_SELECTOR, 'input.form-control.first[placeholder="Input your first name"]')
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, 'input.form-control.second[placeholder="Input your last name"]')
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CSS_SELECTOR, 'input.form-control.third[placeholder="Input your email"]')
    input3.send_keys("123@mail.ru")
    
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

