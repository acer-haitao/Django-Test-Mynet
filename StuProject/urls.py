
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include

from StuApp import views as ht_index
from guestbook import views as guest_views
from comment import views as net163_views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^deleteid',guest_views.deleteid),
    url(r'^delete',guest_views.delete),
    url(r'^save/',guest_views.save),
    url(r'^create',guest_views.create),
    url('^comment/',guest_views.comment),
    url(r'^net163', net163_views.net163),
    url(r'', ht_index.index, name='index'),
]
