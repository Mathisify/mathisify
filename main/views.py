from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def chapterone(request):
    return render(request, 'chapterone.html')


def chaptertwo(request):
    return render(request, 'chaptertwo.html')
