from django.urls import include
from django.urls import re_path
from django.urls import re_path as url
from django.conf.urls import url
from django.urls import path

from . import views


urlpatterns = [
        path('', views.index, name='index'),
        path('books/', views.BookListView.as_view(), name='books'),
]
