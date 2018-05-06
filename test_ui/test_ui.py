from selenium import webdriver
import unittest
import time
import pytest

@pytest.mark.uitest
class TestFormater(unittest.TestCase):
    def test_plain_lowercase(self):
        driver = webdriver.Chrome()
        driver.get("http://127.0.0.1:5000/ui")
        self.poprawny(driver)
        time.sleep(5)
        driver.quit()

    def poprawny(self, driver):
        wyswietla = driver.find_element_by_id('napis')
        print(wyswietla.text)
        self.assertEqual(wyswietla.text, "Witaj swiecie")

    def gmail(self, driver):
        driver.find_element_by_id("znani").Click()
        self.assertEqual()

    def sprawdzimie(self, driver):
        wyswiet_imie = driver.find_element_by_id('imie')
        print(wyswietl_imie.text)
        self.assertEqual(wyswietl_imie.text, "AgnieszkaR")
