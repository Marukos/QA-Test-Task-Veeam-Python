import os
import argparse
import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class TestCases(unittest.TestCase):
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--department', default="Research & Development", type=str)
    parser.add_argument('-v', '--vacancies', default=14, type=int)
    args = parser.parse_args()

    def test_vacancies(self):

        self.department = self.args.department
        self.language = self.args.language
        self.vacancies = self.args.vacancies

        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

        self.driver.get("https://cz.careers.veeam.com/vacancies")
        self.driver.maximize_window()

        accept_cookies = self.driver.find_elements(By.XPATH, "//*[@id=\"cookiescript_accept\"]")

        if len(accept_cookies) > 0:
            accept_cookies[0].click()

        self.driver.find_element(By.XPATH, "//button[@id='sl']").click()

        departments = self.driver.find_elements(
            By.XPATH, "//*[@id=\"root\"]/div/div[1]/div/div/div[1]/div/div[2]/div/div/div/*")

        department_element = None
        for department in departments:
            if department.text == self.department:
                department_element = department
                break

        self.assertIsNotNone(department_element)
        department_element.click()

        list_of_vacancies = self.driver.find_elements(
            By.XPATH, "//*[@id=\"root\"]/div/div[1]/div/div/div[2]/div/*")

        time.sleep(2)
        self.driver.close()
        self.assertEqual(self.vacancies, len(list_of_vacancies))
        print("Test Executed Successfully")


if __name__ == '__main__':
    TestCases().test_vacancies()
