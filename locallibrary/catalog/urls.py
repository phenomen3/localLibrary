from django.urls import include
from django.urls import re_path
from django.urls import re_path as url
from django.conf.urls import url

from . import views


urlpatterns = [
        path('', views.index, name='index'),
]
