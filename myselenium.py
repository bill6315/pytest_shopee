from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest

class sel():
    def __init__(self,driver):
        self.driver = driver
        self.timeout = 10
        self.f = 0.5

    def findElement(self,locator):
        if not isinstance(locator, tuple):
            print('未定位到元素')
        else:
            ele = WebDriverWait(self.driver,self.timeout,self.f).until(EC.presence_of_element_located(locator))
            return ele
    
    def findElements(self,locator):
        if not isinstance(locator, tuple):
                print('未定位到元素')
        else:
            try:

                eles = WebDriverWait(self.driver,self.timeout,self.f).until(EC.presence_of_element_located(locator))
                return eles    
            except:
                return[]

    def sendkeys(self,locator,text=''):
        ele = self.findElement(locator)
        ele.send_keys(text)

    def click(self,locator):
        ele = self.findElement(locator)
        ele.click()

    def claer(self,locator):
        ele = self.findElement(locator)
        ele.claer()
    
    def isElementxist(self,locator):
        try:
            self.findElement(locator)
            return True
        except:
            return False
    
    def get_title(self):
        return self.driver.title

    def get_text(self,locator):
        try:
            ele = self.findElement(locator).text
            return ele
        except:
            return ""


