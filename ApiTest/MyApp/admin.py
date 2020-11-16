from django.contrib import admin


# Register your models here.
from MyApp.models import *

#注册数据表
admin.site.register(DB_tucao)
admin.site.register(DB_home_href)
admin.site.register(DB_project)
admin.site.register(DB_apis)
