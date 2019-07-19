from django.conf.urls import url
#
from . import views
app_name="herotest"
urlpatterns=[
    url("^$",views.index,name="indexes"),
    url("^list/$",views.list,name="list"),
    url(r'^detail/(\d+)/$',views.detail,name="detail"),
    url(r'^heroinfo/(\d+)/$',views.heroinfo,name="heroinfo"),
    url(r'^deletebook/(\d+)/$',views.deletebook,name="deletebook"),
    url(r'^deletehero/(\d+)/$',views.deletehero,name="deletehero"),
    url(r'^newbook/$',views.newbook,name="newbook"),
    url(r'^addhero/(\d+)/$',views.addhero,name="addhero")

]