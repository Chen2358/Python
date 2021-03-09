# coding: utf-8

from PageLocators.loginpage_locators import LoginPageLocators as loc
from Common.basepage import BasePage


class LoginPage(BasePage):
    """页面操作"""

    def login(self, user: object, psd: object) -> object:
        """登录"""
        # WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.username_input_loc))
        doc = "登录页面_登录功能"
        self.wait_eleVisible(loc.username_input_loc, doc=doc)
        self.input_text(loc.username_input_loc, user, doc)
        self.input_text(loc.password_input_loc, psd, doc)
        self.click_element(loc.submit_button_loc, doc)

    def get_errorMsg_from_login(self):
        doc = "登录页面_获取登录区域的错误提示"
        self.wait_eleVisible(loc.error_msg_loc, poll_frequency=0.2, doc=doc)
        return self.get_text(loc.error_msg_text_loc, doc)

