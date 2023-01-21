from myselenium import sel
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import pytest
import allure


login_btn = ('link text','登入')
account_input = ('name','loginKey')
password_input = ('name', 'password')
login_btn2 = ('css selector','[class="wyhvVD _1EApiB hq6WM5 L-VL8Q cepDQ1 _7w24N1"]')
username = ('css selector','[class="navbar__username"]')
search_input = ('css selector','[class="shopee-searchbar-input__input"]')
search_btn = ('xpath','//*[@id="main"]/div/header/div[2]/div/div[1]/div[1]/button')
goods = ('css selector','[class="ie3A+n bM+7UW Cve6sh"]')
add_cart = ('css selector','[class="btn btn-tinted btn--l iFo-rx QA-ylc"]')
cart_btn = ('id','cart_drawer_target_id')
goods_del = ('css selector','[class="-ytT4B"]')
back_home = ('css selector','[class="shopee-svg-icon icon-shopee-logo"]')



class Shopee():

    def __init__(self,driver):
        self.driver = driver

    @allure.step('關閉彈出式視窗') 
    def close_puw(self):
        time.sleep(2)
        ActionChains(self.driver).move_by_offset(200, 100).click().perform()

    @allure.step('網站登入')
    def login(self,account,password):
        sel(self.driver).click(login_btn)
        sel(self.driver).sendkeys(account_input,account)
        sel(self.driver).sendkeys(password_input,password)
        time.sleep(1)
        sel(self.driver).click(login_btn2)

    @allure.step('搜尋商品')
    def search(self,keywords):
        sel(self.driver).sendkeys(search_input,keywords)
        time.sleep(1)
        sel(self.driver).click(search_btn)

    @allure.step('購買商品')
    def shopping(self):
        sel(self.driver).click(goods)
        sel(self.driver).click(add_cart)

    @allure.step('開啟購物車')
    def click_cart_btn(self):
        sel(self.driver).click(cart_btn)

    @allure.step('取消購物車商品')
    def goods_del(self):
        sel(self.driver).click(goods_del)

    @allure.step('回首頁在進入購物車')
    def view_cart1(self):
        sel(self.driver).click(back_home)
        sel(self.driver).click(cart_btn)
    
