# coding: utf-8

from selenium.webdriver.common.by import By


class LoginPageLocators:
    """页面元素定位"""

    username_input_loc = (By.XPATH, '//*[@id="app"]/div/form/div[2]/div/div/input')
    password_input_loc = (By.XPATH, '//*[@id="app"]/div/form/div[3]/div/div/input')
    submit_button_loc = (By.ID, 'btn_login')
    error_msg_loc = (By.XPATH, '//*[@id="app"]/div/form/div[2]/div/div[2]')
    error_msg_text_loc = (By.XPATH, '//*[@id="app"]/div/form/div[2]/div/div[2]')
    message_loc = (By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/section/div[2]/div[1]')