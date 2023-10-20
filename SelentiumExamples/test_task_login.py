import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "https://stepik.org/lesson/236895/step/1"


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage1():

    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        time.sleep(15)
        button = browser.find_element(By.CSS_SELECTOR, "#ember36")
        button.click()
        time.sleep(15)
        input1 = browser.find_element(By.CSS_SELECTOR, "#id_login_email")
        input1.send_keys("borv38@gmail.com")
        input2 = browser.find_element(By.CSS_SELECTOR, "#id_login_password")
        input2.send_keys("passfortestEr6")
        button_dva = browser.find_element(By,CSS_SELECTOR, "#login_form > button")
        button_dva.click()
        time.sleep(15)




