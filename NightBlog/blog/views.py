from django.shortcuts import render
from .models import *


def home(request):
    post = Post.objects.all()
    categories = Category.objects.all()
    return render(request, 'index.html', {"post": post, 'categories': categories})


def post(request, id):
    single_post = Post.objects.get(id=id)
    return render(request, 'post.html', {'single_post': single_post})
