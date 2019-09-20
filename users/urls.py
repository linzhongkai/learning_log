from django.conf.urls import url
from django.contrib.auth.views import login
from . import views

urlpatterns=[
    url(r'^login/$', login, {'template_name':'users/login.html'}, name='login'),
    url(r'^login/$', views.logout_view, name='logout'),
]