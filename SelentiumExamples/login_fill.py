import pytest
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "https://stepik.org/lesson/236895/step/1"
class TestMainPage1():

    def test_guest_should_see_login_link(self, browser):
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
        answer = math.log(int(time.time()))
        print("answer calculated")
        time.sleep(15)
        input3 = browser.find_element(By.CSS_SELECTOR, 'textarea[placeholder="Напишите ваш ответ здесь..."]')
        input3.send_keys(answer)
        button_sub = browser.find_element(By.CSS_SELECTOR, "#ember84 > div > section > div > div.attempt__inner > div.attempt__actions > button")
        button_sub.click()
        time.sleep(15)
        welcome_text_elt = browser.find_element(By.ID, "ember119")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Correct!", welcome_text, "Failed")
        print("passed")
