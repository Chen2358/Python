"""ApiTest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from MyApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcome/', welcome),											#获取菜单	
    re_path('^$',home),                                                 #index页
    path('home/', home),												#首页
    re_path(r"^child/(?P<eid>.+)/(?P<oid>.*)/(?P<ooid>.*)/$", child),	#返回子页面
    path('login/', login),												#登录界面
    path('login_action/', login_action),								#登录
    path('register_action/', register_action),							#注册
    path('accounts/login/', login),										#非登录状态下自动跳回登录界面
    path('logout/', logout),											#退出
    path('pei/', pei),													#匿名吐槽
    path('help/', api_help),											#帮助
    path('project_list/', project_list),								#项目列表
    path('add_project/', add_project),									#增加项目
    path('delete_project/', delete_project),							#删除项目
    re_path(r"apis/(?P<id>.*)/$", open_apis),							#进入项目
    re_path(r"^cases/(?P<id>.*)/$", open_cases),						#进入用例设置
    re_path(r"^project_set/(?P<id>.*)/$", open_project_set),			#进入项目设置
    re_path(r"^save_project_set/(?P<id>.*)/$", save_project_set),		#进入项目设置
    re_path(r"^project_api_add/(?P<Pid>.*)/$", project_api_add),        #新增接口
    re_path(r"^project_api_del/(?P<id>.*)/$", project_api_del),         #删除接口
    path("save_bz/", save_bz),                                          #保存接口备注
    path("get_bz/", get_bz),                                            #获取接口备注
    path("Api_save/", Api_save),                                        #保存接口数据
    path("get_api_data/", get_api_data),                                #获取接口数据
    path("Api_send/", Api_send),                                        #调试弹框发送请求
    path("copy_api/", copy_api),                                        #复制接口
    path("error_request/", error_request),                              #调用异常测试接口
    path("Api_send_home/", Api_send_home),                              #首页发送请求
    path("get_home_log/", get_home_log),                                #获取最新的请求记录
    path("get_api_log_home/", get_api_log_home),                        #获取完整单一请求记录
    re_path(r'^home_log/(?P<log_id>.*)/$', home),                       #带着请求记录再次进入首页
    re_path(r"^add_case/(?P<eid>.*)/$", add_case),                      #新增用例
    re_path(r'^del_case/(?P<eid>.*)/(?P<oid>.*)/$', del_case),          #删除用例
    re_path(r'^copy_case/(?P<eid>.*)/(?P<oid>.*)/$', copy_case),        #复制用例
    path("get_small/", get_small),                                      #获取小用例数据
    path("user_upload/", user_upload),                                  #上传头像
    path("add_new_step/", add_new_step),                                #增加小步骤接口
    re_path(r"^delete_step/(?P<eid>.*)/$", delete_step),                #删除小步骤
    path("get_step/", get_step),                                        #获取小步骤数据
    path("save_step/", save_step),                                      #保存小步骤数据
    path("step_get_api/", step_get_api),                                #步骤详情页获取接口数据
    path("Run_Case/", Run_Case),                                        #运行大用例
    re_path(r"^look_report/(?P<eid>.*)/$", look_report),                #查看报告
    path("save_project_header/", save_project_header),                  #保存请求头
    path("save_case_name/", save_case_name),                            #保存用例名称


]
