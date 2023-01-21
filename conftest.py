import pytest
from selenium import webdriver
import time

@pytest.fixture(scope='session')
def driver(request):
    driver = webdriver.Chrome()
    driver.get('https://shopee.tw/')
    driver.delete_all_cookies()
    time.sleep(1)

    def end():
        driver.delete_all_cookies()
        driver.quit()
    request.addfinalizer(end)
    return driver

