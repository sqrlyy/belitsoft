from selenium import webdriver
from time import sleep
import unittest


class ConversionTest(unittest.TestCase):
    URL = 'https://www.metric-conversions.org/'
    PATH = r'C:\Users\Maksim\PycharmProjects\belitsoft\task_c\chromedriver.exe'

    def test_celse_to_fahr(self):
        driver = webdriver.Chrome(self.PATH)
        driver.get(self.URL)
        sleep(1)
        driver.find_element_by_xpath("//a[text()='Celsius to Fahrenheit']").click()
        driver.find_element_by_id('argumentConv').send_keys(50)
        result = driver.find_element_by_id('answer')
        self.assertEqual(result.text, '50°C= 122.0000°F')

    def test_meters_to_feet(self):
        driver = webdriver.Chrome(self.PATH)
        driver.get(self.URL)
        driver.find_element_by_xpath("//a[text()='Meters to Feet']").click()
        driver.find_element_by_id('argumentConv').send_keys(50)
        result = driver.find_element_by_id('answer')
        self.assertEqual(result.text, '50m= 164ft 0.5039400in')

    def test_ounces_to_grams(self):
        driver = webdriver.Chrome(self.PATH)
        driver.get(self.URL)
        sleep(1)
        driver.find_element_by_xpath("//a[text()='Weight']").click()
        driver.find_element_by_xpath("//a[text()='Ounces to Grams']").click()
        driver.find_element_by_id('argumentConv').send_keys(50)
        result = driver.find_element_by_id('answer')
        self.assertEqual(result.text, '50oz= 1417.476g')


if __name__ == '__main__':
    unittest.main()
