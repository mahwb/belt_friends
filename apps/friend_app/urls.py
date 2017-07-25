from django.conf.urls import url
from . import views

app_name="friend"
urlpatterns = [
    url(r'^$', views.index, name="idx"),
    url(r'^user$', views.user, name="user"),
    url(r'^add$', views.add, name="add"),
    url(r'^new/(?P<id>\d+)$', views.new, name="new"),
    url(r'^delete/(?P<id>\d+)$', views.delete, name="del")
]
