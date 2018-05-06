from selenium import webdriver
import unittest
import time
import pytest

@pytest.mark.uitest
class TestFormater(unittest.TestCase):
    def test_plain_lowercase(self):
        driver = webdriver.Chrome()
        driver.get("http://127.0.0.1:5000/ui")
        self.is_greatings_visible(driver)
        self.is_name_present(driver)
        self.is_google_integration_works(driver)
        #time.sleep(5)
        driver.quit()

    def is_greatings_visible(self, driver):
        wyswietla = driver.find_element_by_id('napis')
        print(wyswietla.text)
        self.assertEqual(wyswietla.text, "Witaj swiecie")

    def is_name_present(self, driver):
        wyswiet_imie = driver.find_element_by_id('imie')
        print(wyswietl_imie.text)
        self.assertEqual(wyswietl_imie.text, "AgnieszkaR")

    def is_google_integration_works(self, driver):
        driver.find_element_by_id("znani").Click()
        #wait = WebDriverWait(driver, 2)
        #WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, "res")))
