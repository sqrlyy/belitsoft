from selenium import webdriver
from time import sleep

URL = 'https://www.metric-conversions.org/'
PATH = r'C:\Users\Maksim\PycharmProjects\belitsoft\task_c\chromedriver.exe'


def celse_to_fahr():
    driver = webdriver.Chrome(PATH)
    driver.get(URL)
    sleep(1)
    driver.find_element_by_xpath("//a[text()='Celsius to Fahrenheit']").click()
    driver.find_element_by_id('argumentConv').send_keys(50)
    result = driver.find_element_by_id('answer')
    assert result.text == '50°C= 122.0000°F'


def meeters_to_feet():
    driver = webdriver.Chrome(PATH)
    driver.get(URL)
    driver.find_element_by_xpath("//a[text()='Meeters to Feet']").click()
    driver.find_element_by_id('argumentConv').send_keys(50)
    result = driver.find_element_by_id('answer')
    assert result.text == '50m= 164ft 0.5039400in'


def ounces_to_grams():
    driver = webdriver.Chrome(PATH)
    driver.get(URL)
    sleep(1)
    driver.find_element_by_xpath("//a[text()='Weight']").click()
    driver.find_element_by_xpath("//a[text()='Ounces to Grams']").click()
    driver.find_element_by_id('argumentConv').send_keys(50)
    result = driver.find_element_by_id('answer')
    assert result.text == '50oz= 1417.476g'
