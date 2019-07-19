from django.conf.urls import url
#
from . import views
app_name="newvote"
urlpatterns=[
    url(r'^$',views.index,name="indexes"),
    url(r'^list/(\d+)/$',views.list,name="list"),
    url(r'^result/(\d+)/$',views.result,name="result"),
    url(r'^newquestion/$', views.newquestion, name='newquestion'),
    url(r'^addchouse/(\d+)/$', views.addchouse, name='addchouse'),
    url(r'^login/$',views.login,name='login'),
    url(r'^regist$',views.regist,name='regist'),
    url(r'^logout/$',views.logout,name='logout'),
]
