from django.conf.urls import url
from . import views

app_name="sellfresh"
urlpatterns=[
    url(r"^$",views.Index.as_view(),name='index'),
    url(r'^regist/$',views.regist,name='regist'),
    url(r'^login/$',views.login,name='login'),
    url(r'^logout/$',views.logout,name='logout'),
    url(r'^checkuser/$',views.checkuser,name='checkuser'),
    url(r'^usercenter/$',views.Usercenter.as_view(),name='usercenter'),
    url(r'^verify/$', views.verify, name='verify')
]