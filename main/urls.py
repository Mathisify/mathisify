from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('chapterone/', views.chapterone),
    path('about/', views.about),
    path('compandint/', views.compandint),
    path('chapterzero/', views.chapterzero),
    path('chapterzero2/', views.chapterzero2),
    path('welcometoscratch/', views.welcometoscratch),
    path('search/', views.search),
    path('diginfo/', views.diginfo),
    path('elements/', views.elements),
    path('workshops/', views.workshops),
    path('histcomp/', views.histcomp),
    path('index2/', views.index2),
    path('firstprogram/', views.firstprogram),
]
