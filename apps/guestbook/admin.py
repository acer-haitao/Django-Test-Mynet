from django.contrib import admin

# Register your models here.
from apps.guestbook.models import Msg
admin.site.register(Msg)