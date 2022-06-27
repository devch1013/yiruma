from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.student_home, name='student_home'),
    path('create', views.student_create, name='student_create'),
    path('<str:id>', views.student_detail, name='student_detail'),
    path('<str:id>/edit', views.student_edit, name='student_edit'),
]
