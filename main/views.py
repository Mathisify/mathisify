from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def chapterone(request):
    return render(request, 'chapterone.html')


def about(request):
    return render(request, 'about.html')


def compandint(request):
    return render(request, 'compandint.html')
