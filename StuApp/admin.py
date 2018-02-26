from django.contrib import admin

# Register your models here.
#再次注册后后台才能看到对应的数据库
from StuApp.models import URLDB,TabName
admin.site.register(URLDB)
admin.site.register(TabName)