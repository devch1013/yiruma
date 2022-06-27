from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.money_home, name='money_home'),
    path('create', views.money_create, name='money_create'),
    path('<str:id>', views.money_detail, name='money_detail'),
    path('<str:id>/edit', views.money_edit, name='money_edit'),
]
