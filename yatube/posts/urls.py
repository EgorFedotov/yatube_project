from tokenize import group
from django.urls import URLPattern, path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name="index"),
    path('group/<slug:slug>/', views.group_posts, name='group_list')
]