from django.contrib import admin
from django.urls import path
from recipe import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.main, name='main'),
    path('categories/', views.category_list, name='category_list')
]
