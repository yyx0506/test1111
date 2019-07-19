from django.conf.urls import url
from . import views

app_name="sellfresh"
urlpatterns=[
    url(r"^$", views.Index.as_view(), name='index'),
    url(r'^regist/$', views.regist, name='regist'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^checkuser/$', views.checkuser, name='checkuser'),
    url(r'^usercenter/$', views.Usercenter.as_view(), name='usercenter'),
    url(r'^verify/$', views.verify, name='verify'),
    url(r'^cart/$',views.Cartlist.as_view(),name='cart'),
    url(r'^order/$',views.Orderlist.as_view(),name='order'),
    url(r'^site/$',views.AddAddress.as_view(),name='address'),
    url(r'^alladdress/$',views.Alladdress.as_view(),name='alladdress'),
    url(r'^addgoods/$',views.Addgoodscart.as_view(),name='addgoods'),
    url(r'^edit/$',views.edit,name='edit'),
    url(r'^deletegoods/$',views.deletegoods,name="deletegoods"),
    url(r'^getorder/$',views.Getorder.as_view(),name="getorder"),
    url(r'^myorder/$',views.Zhifudingdan.as_view(),name='myorder'),
    url(r'^orderagain/$',views.Orderagain.as_view(),name='orderagain'),
    url(r'^updateorder/$',views.Updateorder.as_view(),name="updateorder"),
    url(r'^commit/$',views.Commint.as_view(),name='commit')

]