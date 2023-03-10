from myselenium import sel
from selenium import webdriver
from shopee import Shopee
import time
import pytest
import allure
import os


account = 'account'
password = 'password'
keywords = 'python'
myname = ('css selector','[class="navbar__username"]')
goods_name = ('css selector','[class="ie3A+n bM+7UW Cve6sh"]')
cart_goods_name = ('css selector','[class="kjRybG"]')


@pytest.fixture(scope='module')
def shopee(driver):
    return Shopee(driver)   

@allure.step('測試蝦皮網站開啟是否成功')
def test_web_open(driver):
    tit = driver.title
    assert tit == '蝦皮購物 | 花得更少買得更好' , '開啟網頁失敗'
        
@allure.step('測試帳號登入是否成功')
def test_login(driver,shopee):
    shopee.close_puw()
    shopee.login(account,password)
    ele = sel(driver).get_text(myname)
    assert ele == '2uvcxuaeao' , '登入失敗'

@allure.step('測試商品是否成功加入購物車')
def test_add_goods(driver,shopee):
    shopee.search(keywords)
    ele = sel(driver).get_text(goods_name)
    shopee.shopping()
    shopee.close_puw()
    shopee.click_cart_btn()
    ele2 = sel(driver).get_text(cart_goods_name)
    assert ele == ele2 , '加入購物車失敗'

@allure.step('測試購物車商品是否成功取消')
def test_good_del_1(driver,shopee):
    shopee.goods_del()
    shopee.view_cart1()
    ele = sel(driver).isElementxist(cart_goods_name)
    assert ele == False , '商品未取消成功'
 
@allure.step('測試購物車商品是否成功取消')
def test_good_del_2(driver,shopee):
    shopee.goods_del()  
    driver.refresh()
    ele = sel(driver).isElementxist(cart_goods_name)
    assert ele == False  ,'商品未取消成功'

if __name__ == '__main__':
    pytest.main(['--alluredir=./test_report','test_shopee.py'])
    os.system(r'allure serve ./test_report')
    




