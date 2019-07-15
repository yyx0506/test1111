from django.conf.urls import url
from . import views
app_name="comment"
urlpatterns=[
    url(r'^comment/(\d+)/$',views.Allcommment.as_view(),name='comment')
]