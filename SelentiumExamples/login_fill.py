import pytest
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = f"https://stepik.org/lesson/{tempor}/step/1"
class TestMainPage1():

    @pytest.mark.parametrize('tempor', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
    def test_guest_should_see_login_link(self, browser, tempor):
        browser.get(link)
        button = browser.find_element(By.ID, "ember33")
        button.click()
        print("\nButton found, clicked")
        input1 = browser.find_element(By.ID, "id_login_email")
        input1.send_keys("borv38@gmail.com")
        input2 = browser.find_element(By.ID, "id_login_password")
        input2.send_keys("passfortestEr6")
        button_dva = browser.find_element(By.CSS_SELECTOR, "#login_form > button")
        button_dva.click()
        input3 = browser.find_element(By.CSS_SELECTOR, 'textarea[placeholder="Напишите ваш ответ здесь..."]')
        input3.clear()
        input3.send_keys(math.log(int(time.time())))
        print("ответ введен")
        button_sub = browser.find_element(By.CSS_SELECTOR, "button.submit-submission")
        button_sub.click()
        print("button pressed")
        time.sleep(10)
        welcome_text_elt = browser.find_element(By.CSS_SELECTOR, "p.smart-hints__hint")
        welcome_text = welcome_text_elt.text
        assert "Correct!" == welcome_text, "not passed"
        print("passed")
        time.sleep(10)