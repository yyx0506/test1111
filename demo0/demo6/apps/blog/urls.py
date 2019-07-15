from . import views
from django.conf.urls import url
app_name="blog"
urlpatterns=[
    url(r'^$', views.blog, name='blog'),
    url(r'^single/(\d+)/$',views.Single.as_view(),name='single'),
    url(r'^addarticle/$',views.Addartical.as_view(),name='addrical'),
    url(r'^archives/(\d+)/(\d+)/$',views.Archives.as_view(),name='archives'),
    url(r'^cateart/(\d+)/$',views.Cateart.as_view(),name='cateart'),
    url(r'^tagart/(\d+)/$',views.Tagart.as_view(),name='tagart'),
    url(r'^login/$',views.login,name='login'),
    url(r'^regist/$',views.regist,name='regist'),
    url(r'^logout/$',views.logout,name='logout'),
    url(r'^verify/',views.verify,name='verify'),
    url(r'^checkuser/$',views.checkuser,name='checkuser'),

]