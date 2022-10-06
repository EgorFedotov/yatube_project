from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

# Create your views here.

def index(request):
    return HttpResponse('Самая главная страница')

def group_posts(request, any_slug):
    return HttpResponse('Тут будут посты')
