from django.contrib import admin

# Register your models here.
from guestbook.models import Msg
admin.site.register(Msg)