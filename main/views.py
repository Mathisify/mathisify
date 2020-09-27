from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from .models import Post, View


def index(request):
    views = View.objects.all()
    return render(request, 'index.html', {'views': views})


def chapterone(request):
    views = View.objects.all()
    return render(request, 'chapterone.html', {'views': views})


def about(request):
    views = View.objects.all()
    return render(request, 'about.html', {'views': views})


def compandint(request):
    views = View.objects.all()
    return render(request, 'compandint.html', {'views': views})

def histcomp(request):
    views = View.objects.all()
    return render(request, 'histcomp.html', {'views': views})


def chapterzero(request):
    views = View.objects.all()
    return render(request, 'chapterzero.html', {'views': views})

def chapterzero2(request):
    views = View.objects.all()
    return render(request, 'chapterzero2.html', {'views': views})


def welcometoscratch(request):
    views = View.objects.all()
    return render(request, 'welcometoscratch.html', {'views': views})

def diginfo(request):
    views = View.objects.all()
    return render(request, 'diginfo.html', {'views': views})

def index2(request):
    views = View.objects.all()
    return render(request, 'index2.html', {'views': views})

def elements(request):
    views = View.objects.all()
    return render(request, 'elements.html', {'views': views})
    
def ifstate(request):
    views = View.objects.all()
    return render(request, 'ifstate.html', {'views': views})

def firstprogram(request):
    views = View.objects.all()
    return render(request, 'firstprogram.html', {'views': views})

def workshops(request):
    if request.user.is_authenticated:
        return render(request, 'workshops.html', {'views': views})
    else:
        return redirect('/accounts/register/')


def search(request):
    query = request.GET['query']
    posts = Post.objects.filter(title__icontains = query)
    params = {'posts': posts}
    return render(request, 'search.html', params)
