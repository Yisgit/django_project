from django.conf.urls import url,include
from django.contrib import admin
from django.views.generic import ListView, DetailView
from cameraui.models import Cam12pr
from . import views
urlpatterns =[
    url(r'^', views.preset_view, name="cam12pr"),
]
