from django.shortcuts import render, get_object_or_404

from .models import Post, Group

LAST_POSTS = 10


def index(request):
    template = 'posts/index.html'
    posts = Post.objects.all()[:LAST_POSTS]
    title = 'Последние обновления на сайте'
    context = {
        'title': title,
        'posts': posts
    }
    return render(request, template, context)


def group_posts(request, slug):
    template = 'posts/group_list.html'
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()
    title = f'Записи сообщества {group}'
    context = {
        'title': title,
        'description': group.description,
        'posts': posts
    }

    return render(request, template, context)
