from django.shortcuts import render, get_object_or_404
from .models import Post, Group

COUNT_POSTS: int = 10


def index(request):
    title = 'Последние обновления на сайте'
    posts = Post.objects.order_by('-pub_date')[:COUNT_POSTS]
    context = {
        'title': title,
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    title = 'Записи сообщества'
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:COUNT_POSTS]
    context = {
        'title': title,
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)