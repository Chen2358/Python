# coding: utf-8


from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageLocators.loginpage_locators import LoginPageLocators as loc


class IndexPage:
    """登录后dashboard"""

    def __init__(self, driver):
        self.driver = driver

    def isExist_logout_ele(self):
        # 判断出错提示信息是否出现
        try:
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.message_loc))
            return True
        except:
            return False
