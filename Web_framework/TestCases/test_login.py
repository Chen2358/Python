# coding:utf-8

import pytest
# import ddt
from PageObjects.index_page import IndexPage
from TestDatas import login_datas as LD


@pytest.mark.usefixtures("access_web")                      #类级别只运行一次
@pytest.mark.usefixtures("refresh_page")                    #函数级别则表示该类中每个case都用
class TestLogin:

    """
    @classmethod
    def setUpClass(cls) -> None:
        # 所有测试用例之前的，setup===整个测试类只执行一次
        cls.driver = webdriver.Chrome(
            executable_path='D:\\Tester\Scripts\\Web_framework\\browser_driver\\chromedriver.exe')
        cls.driver.get(CD.web_login_url)
        cls.driver.maximize_window()
        cls.lg = LoginPage(cls.driver)

    @classmethod
    def tearDownClass(cls) -> None:
        # 所有测试用例之后的，teardown===整个测试类只执行一次
        cls.driver.quit()


    # def setUp(self) -> None:
    """

    # 异常用例---手机号格式错误
    # @ddt.data(*LD.phone_data)  # unittest使用ddt数据驱动
    @pytest.mark.demo
    @pytest.mark.parametrize("data", LD.phone_data)  # pytest 中参数化
    def test_login_0_user_wrongFormat(self, data, access_web):
        access_web[1].login(data["user"], data["psd"])
        assert access_web[1].get_errorMsg_from_login() == data["check"]

    # 正常用例：登录成功
    @pytest.mark.smoke
    def test_login_1_success(self, access_web):                     # fixture的函数名称代表返回值
        access_web[1].login(LD.success_data["user"], LD.success_data["psd"])
        # 断言是否登录成功
        assert IndexPage(access_web[0]).isExist_logout_ele()


