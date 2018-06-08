from django.conf.urls import url
from . import views
from django.views.generic import ListView, DetailView
from cameraui.models import Cam12pr

urlpatterns = [
    url(r'^12cam/', views.cam12, name='cam12'),
    url(r'^13cam/', views.cam13, name='cam13'),
    url(r'^14cam/', views.cam14, name='cam14'),
    url(r'^somethinghgfst544wvet56/', views.my_lab, name='my_lab_run'),
    url(r'^$', views.index, name='index'),
]
