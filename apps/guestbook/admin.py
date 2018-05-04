from django.contrib import admin
from apps.guestbook.models import Msg

@admin.register(Msg)
class MsgAdmin(admin.ModelAdmin):
    list_display = ('time','username','txt','title')
    list_per_page = 100
    list_filter = ('time','username','txt','title')
    search_fields = ('time','username','txt','title')