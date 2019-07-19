from django.conf.urls import url
from . import views
app_name="cellmall"
urlpatterns=[
    url('^$',views.index,name="indexes"),
    url('^login/$',views.login,name='login'),
    url('^logout/$',views.logout,name='logout'),
    url('^register/$',views.register,name="register")
]