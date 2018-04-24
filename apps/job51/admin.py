from django.contrib import admin
from apps.job51.models import job51
# Register your models here.

#后台显示
@admin.register(job51)
class job51Admin(admin.ModelAdmin):
    #显示
    list_display = ('id','job','company','address','wages','date','jobname','joburl','jobaddress')
    #显示条数
    list_per_page = 50
    #显示排序
    ordering=('-date',)
    #显示编辑
    #list_editable = ['jobname']
    #过滤
    list_filter = ('job','address','wages','date','jobname','jobaddress')
    search_fields = ('job','company','address','wages','date','jobname','jobaddress')
    #date_hierarchy = 'date'