from django.conf.urls import url
from . import views

app_name="goods"
urlpatterns=[
    url(r"^goodsdetail/(\d+)/$",views.Detail.as_view(),name='detail'),
    url(r"^goodslist/(\d+)/(\d+)/$",views.List.as_view(),name='list'),
    url(r'^comment/(\d+)/$',views.GoodComment.as_view(),name='comment'),


]