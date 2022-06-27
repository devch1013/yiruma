from django.shortcuts import render, redirect
from django.db.models import Q

# Create your views here.


def home(request):
  return render(request, 'home.html')