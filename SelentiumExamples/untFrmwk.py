import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class TestAbs(unittest.TestCase):
    def setUp(self): 
        self.driver = webdriver.Chrome()


    def test_theform1(self):
        browser = self.driver
        browser.get("http://suninjuly.github.io/registration1.html")
        input1 = browser.find_element(By.CSS_SELECTOR, 'input.form-control.first[placeholder="Input your first name"]')
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.CSS_SELECTOR, 'input.form-control.second[placeholder="Input your last name"]')
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.CSS_SELECTOR, 'input.form-control.third[placeholder="Input your email"]')
        input3.send_keys("123@mail.ru")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Fucking error")
        print("passed")
        time.sleep(10)
        browser.quit()


    def test_theform2(self):
	    browser = self.driver
	    browser.get("http://suninjuly.github.io/registration2.html")
	    input1 = browser.find_element(By.CSS_SELECTOR, 'input.form control.first[placeholder="Input your first name"]')
	    input1.send_keys("Ivan")
	    input2 = browser.find_element(By.CSS_SELECTOR, 'input.form-control.second[placeholder="Input your last name"]')
	    input2.send_keys("Petrov")
	    input3 = browser.find_element(By.CSS_SELECTOR, 'input.form-control.third[placeholder="Input your email"]')
	    input3.send_keys("123@mail.ru")
	    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
	    button.click()
	    self.time.sleep(1)
	    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
	    welcome_text = welcome_text_elt.text
	    self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "ucking Error")
	    time.sleep(10)
	    browser.quit()

if __name__ == "__main__":
    unittest.main()