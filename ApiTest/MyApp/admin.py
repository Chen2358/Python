from django.contrib import admin


# Register your models here.
from MyApp.models import *

#注册数据表
admin.site.register(DB_tucao)
admin.site.register(DB_home_href)
admin.site.register(DB_project)
admin.site.register(DB_apis)
admin.site.register(DB_apis_log)
admin.site.register(DB_cases)
admin.site.register(DB_step)
admin.site.register(DB_project_header)
