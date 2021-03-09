# coding:utf-8

# 正确的用户名、密码
success_data = {"user":"test@sogaa.net", "psd": "root@123456"}

# 异常数据
phone_data = [
    {"user": " ", "psd": " ", "check": "请输入正确手机号/邮箱"},
    {"user": "test", "psd": "123123", "check": "请输入正确手机号/邮箱"}
]