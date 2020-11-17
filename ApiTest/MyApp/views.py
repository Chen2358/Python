from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from MyApp.models import *
import json




def welcome(request):
	return render(request, 'welcome.html')

#控制不同的页面返回不同的数据：数据分发器
def child_json(eid, oid=''):
	res = {}
	if eid == 'home.html':
		data = DB_home_href.objects.all()
		res = {"hrefs": data}
	if eid == 'project_list.html':
		data = DB_project.objects.all()
		res = {"projects": data}

	if eid == 'P_apis.html':
		project = DB_project.objects.filter(id=oid)[0]
		apis = DB_apis.objects.filter(project_id=oid)
		res = {"project": project, 'apis': apis}

	if eid == 'P_cases.html':
		project = DB_project.objects.filter(id=oid)[0]
		res = {"project": project}

	if eid == 'P_project_set.html':
		project = DB_project.objects.filter(id=oid)[0]
		res = {"project": project}

	return res

#返回子页面
def child(request, eid, oid):
	res = child_json(eid, oid)
	return render(request, eid, res)



def login(request):
	return render(request, 'login.html')

#登录
def login_action(request):
	u_name = request.GET['username']
	p_word = request.GET['password']

	#连通django用户表验证用户名、密码
	from django.contrib import auth

	user = auth.authenticate(username=u_name, password=p_word)
	if user is not None:
		#正确时
		# return HttpResponseRedirect('/home/')
		auth.login(request, user)
		request.session['user'] = u_name
		return HttpResponse('成功')
	else:
		#错误时
		return HttpResponse('失败')

#注册
def register_action(request):
	u_name = request.GET['username']
	p_word = request.GET['password']

	#连通django用户表，验证用户名、密码
	from django.contrib.auth.models import User

	try:
		user = User.objects.create_user(username=u_name, password=p_word)
		user.save()
		return HttpResponse('注册成功')
	except:
		return HttpResponse('注册失败~用户名已存在')

#首页
@login_required
def home(request):
    return render(request,'welcome.html',{"whichHTML": "home.html","oid": ""})

#退出
def logout(request):
	from django.contrib import auth
	auth.logout(request)
	return HttpResponseRedirect('/login/')

#吐槽
def pei(request):
	tucao_text = request.GET['tucao_text']
	#写入数据库
	DB_tucao.objects.create(user=request.user.username, text=tucao_text)
	return HttpResponse('')

#帮助
def api_help(request):
	return render(request, 'welcome.html', {"whichHTML": "help.html", "oid": ""})

#项目列表
def project_list(request):
	return render(request, 'welcome.html', {"whichHTML": "project_list.html", "oid": ""})

#新增项目
def add_project(request):
	project_name = request.GET['project_name']
	DB_project.objects.create(name=project_name,remark='', user=request.user.username, other_user='')
	return HttpResponse('')

#删除项目
def delect_project(request):
	id = request.GET['id']
	DB_project.objects.filter(id=id).delete()
	DB_apis.objects.filter(project_id=id).delete()		#删除项目中的接口
	return HttpResponse('')

#进入接口库
def open_apis(request, id):
	project_id = id
	return render(request, 'welcome.html', {"whichHTML": "P_apis.html", "oid": project_id})


#进入用例设置
def open_cases(request, id):
	project_id = id
	return render(request, 'welcome.html', {"whichHTML": "P_cases.html", "oid": project_id})


#进入项目设置	
def open_project_set(request, id):
	project_id = id
	return render(request, 'welcome.html', {"whichHTML": "P_project_set.html", "oid": project_id})


#保存项目设置	
def save_project_set(requset, id):
    project_id = id
    name = requset.GET['name']
    remark = requset.GET['remark']
    other_user = requset.GET['other_user']
    DB_project.objects.filter(id=project_id).update(name=name,remark=remark,other_user=other_user)
    return HttpResponse('')

#新增接口
def project_api_add(request, Pid):
    project_id = Pid
    DB_apis.objects.create(project_id=project_id)
    return HttpResponseRedirect('/apis/%s/'%project_id)

#删除接口
def project_api_del(request,id):
    project_id = DB_apis.objects.filter(id=id)[0].project_id 			#根据接口ID查找所属项目ID
    DB_apis.objects.filter(id=id).delete() 								#删除接口
    return HttpResponseRedirect('/apis/%s/'%project_id)					#返回重定向的初始路由

#保存接口备注
def save_bz(request):
	api_id = request.GET['api_id']
	bz_value = request.GET['bz_value']
	DB_apis.objects.filter(id=api_id).update(des=bz_value)				#更新数据库中接口备注
	return HttpResponse('')

#获取接口备注
def get_bz(request):
	api_id = request.GET['api_id']
	bz_value = DB_apis.objects.filter(id=api_id)[0].des
	return HttpResponse(bz_value)

#保存接口数据
def Api_save(request):
    # 提取所有数据
    api_id = request.GET['api_id']
    ts_method = request.GET['ts_method']
    ts_url = request.GET['ts_url']
    ts_host = request.GET['ts_host']
    ts_header = request.GET['ts_header']
    ts_body_method = request.GET['ts_body_method']
    ts_api_body = request.GET['ts_api_body']
    api_name = request.GET['api_name']
    # 保存数据
    DB_apis.objects.filter(id=api_id).update(
        api_method = ts_method,
        api_url = ts_url,
        api_header = ts_header,
        api_host = ts_host,
        body_method = ts_body_method,
        api_body = ts_api_body,
        name = api_name
    )
    # 返回
    return HttpResponse('success')

#获取接口数据
def get_api_data(request):
	api_id = request.GET['api_id']
	api = DB_apis.objects.filter(id=api_id).values()[0]
	return HttpResponse(json.dumps(api), content_type='application/child_json')
