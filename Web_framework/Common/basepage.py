# coding:utf-8

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import datetime
import time

from Common import dir_config


class BasePage:
    """封装基本函数：执行日志、异常处理、失败截图及所有页面的公共部分"""

    def __init__(self, driver):
        self.driver = driver

    # 等待元素可见
    def wait_eleVisible(self, locator, wait_times=20, poll_frequency=0.5, doc=""):
        """

        :param locator:元素
        :param times:等待时长
        :param poll_frequency:轮询时间
        :param doc:模块名_页面名称_操作名称
        :return: None
        """
        logging.info("等待元素 {0} 可见".format(locator))
        try:
            # 开始等待时间
            start = datetime.datetime.now()
            WebDriverWait(self.driver, wait_times, poll_frequency).until(EC.visibility_of_element_located(locator))
            # 结束等待时间
            end = datetime.datetime.now()
            # 等待时间写入日志
            wait_times = (end - start).seconds
            logging.info("{0}: 元素 {1} 已可见, 起始时间: {2}, 结束时间{3}, 等待时长为：{4}".format(doc, locator, start, end, wait_times))
        except:
            logging.exception("等待元素可见失败！！！")
            # 截图
            self.save_screenshot(doc)
            raise

    # 等待元素存在
    def wai_elePresence(self):
        pass

    # 查找元素
    def get_element(self, locator, doc=""):
        logging.info("查找元素 {0}".format(locator))
        try:
            return self.driver.find_element(*locator)
        except:
            logging.exception("查找元素失败！！！")
            # 截图
            self.save_screenshot(doc)
            raise

    # 点击操作
    def click_element(self, locator, doc=""):
        ele = self.get_element(locator, doc)
        logging.info("{0} 点击元素: {1}".format(doc, locator))
        try:
            ele.click()
        except:
            logging.exception("元素点击操作失败！！！")
            # 截图
            self.save_screenshot(doc)
            raise

    # 输入操作
    def input_text(self, locator, text, doc=""):
        ele = self.get_element(locator, doc)
        logging.info("输入文本".format(doc, locator))
        try:
            ele.send_keys(text)
        except:
            logging.exception("输入操作失败！！！")
            # 截图
            self.save_screenshot(doc)
            raise

    # 获取元素文本内容
    def get_text(self, locator, doc=""):
        ele = self.get_element(locator, doc)
        logging.info("获取{0}元素文本".format(locator))
        try:
            return ele.text
        except:
            logging.exception("获取元素文本失败！！！")
            # 截图
            self.save_screenshot(doc)
            raise

    # 获取元素属性
    def get_element_attribute(self,locator, attr, doc=""):
        ele = self.get_element(locator, doc)
        logging.info("获取 {0} 元素 {1} 属性".format(locator,attr))
        try:
            return ele.get_attribute(attr)
        except:
            logging.exception("获取元素属性失败！！！")
            # 截图
            self.save_screenshot(doc)
            raise

    # alert 处理
    def alert_action(self, action="accept"):
        pass

    # iframe 操作
    def switch_iframe(self, iframe_reference):
        pass

    # 上传文件
    def upload_file(self):
        pass

    # 截图
    def save_screenshot(self, doc):
        # 图片名称：模块名_页面名称_操作名称_年-月-日_时分秒.png
        filePath = dir_config.screenshot_dir + \
                    "{0}_{1}.png".format(doc, time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()))
        try:
            self.driver.save_screenshot(filePath)
            logging.info("截图成功。文件路径为: {0}".format(filePath))
        except:
            logging.exception("截图失败")
        return filePath

