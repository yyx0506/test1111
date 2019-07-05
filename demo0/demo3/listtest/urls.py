from django.conf.urls import url
from . import views


app_name='listtest'
urlpatterns=[
    url(r'^$', views.index, name='index'),
    url(r'^list/(\d+)/$', views.list, name='list'),
    url(r'^result/(\d+)/$', views.result, name='result'),
    url(r'^newquestion/$',views.newquestion,name='newquestion'),
    url(r'^addchouse/(\d+)/$',views.addchouse,name='addchouse')
]