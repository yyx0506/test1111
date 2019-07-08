from django.conf.urls import url,include
from . import views


app_name='booktest'
urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^list/$',views.Listview.as_view(),name='list'),
    # url(r'^list/$',views.list,name='list'),
    url(r'^detail/(\d+)/$',views.detail,name='detail'),
    url(r'^deletehero/(\d+)/$',views.deletehero,name='deletehero'),
    url(r'^deletebook/(\d+)/$',views.deletebook,name='deletebook'),
    url(r'^addhero/(\d+)/$',views.addhero,name='addhero'),
    url(r'^addimg/$',views.Addimg.as_view(),name='addimg')
]