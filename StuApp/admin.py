from django.contrib import admin

# Register your models here.
from StuApp.models import URLDB,TabName
admin.site.register(URLDB)
admin.site.register(TabName)