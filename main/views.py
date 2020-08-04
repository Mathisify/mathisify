from django.shortcuts import render
from .models import Post


def index(request):
    return render(request, 'index.html')


def chapterone(request):
    return render(request, 'chapterone.html')


def about(request):
    return render(request, 'about.html')


def compandint(request):
    return render(request, 'compandint.html')


def chapterzero(request):
    return render(request, 'chapterzero.html')


def welcometoscratch(request):
    return render(request, 'welcometoscratch.html')

def diginfo(request):
    return render(request, 'diginfo.html')

def elements(request):
    return render(request, 'elements.html')

def workshops(request):
    return render(request, 'workshops.html')


def search(request):
    query = request.GET['query']
    posts = Post.objects.filter(title__icontains = query)
    params = {'posts': posts}
    return render(request, 'search.html', params)
