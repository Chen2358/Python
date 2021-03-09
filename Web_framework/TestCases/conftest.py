# coding:utf-8

import pytest
from selenium import webdriver

from PageObjects.login_page import LoginPage
from TestDatas import Common_Datas as CD

"""fixture，该文件必须与case放在一级"""

driver = None


# 声明为fixture
@pytest.fixture(scope="class")
def access_web():
    global driver
    # 前置操作
    driver = webdriver.Chrome(
        executable_path='D:\\Tester\Scripts\\Web_framework\\browser_driver\\chromedriver.exe')
    driver.get(CD.web_login_url)
    driver.maximize_window()
    lg = LoginPage(driver)
    yield driver, lg                #返回值
    # 后置操作
    driver.quit()


@pytest.fixture
def refresh_page():
    # 前置操作
    global driver
    yield
    # 后置操作
    driver.refresh()
