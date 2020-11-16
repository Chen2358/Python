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
    path('home/', home),												#首页
    re_path(r"^child/(?P<eid>.+)/(?P<oid>.*)/$", child),				#返回子页面
    path('login/', login),												#登录界面
    path('login_action/', login_action),								#登录
    path('register_action/', register_action),							#注册
    path('accounts/login/', login),										#非登录状态下自动跳回登录界面
    path('logout/', logout),											#退出
    path('pei/', pei),													#匿名吐槽
    path('help/', api_help),											#帮助
    path('project_list/', project_list),								#项目列表
    path('add_project/', add_project),									#增加项目
    path('delect_project/', delect_project),							#删除项目
    re_path(r"apis/(?P<id>.*)/$", open_apis),							#进入项目
    re_path(r"^cases/(?P<id>.*)/$", open_cases),						#进入用例设置
    re_path(r"^project_set/(?P<id>.*)/$", open_project_set),			#进入项目设置
    re_path(r"^save_project_set/(?P<id>.*)/$", save_project_set),		#进入项目设置
    re_path(r"^project_api_add/(?P<Pid>.*)/$", project_api_add),        #新增接口
]
