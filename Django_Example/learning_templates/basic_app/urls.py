from django.conf.urls import url
from basic_app import views

#Template Tagging
app_name = 'basic_app' #used in relative_url_templates file to compare

urlpatterns = [
    url(r'^relative/$',views.relative,name='relative'),
    url(r'^other/$',views.other,name='other'),
]
