from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'William Tjen',
        'title' : 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 08, 2021'
    },
    {
        'author': 'Evelyn Leonard',
        'title' : 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 07, 2021'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')