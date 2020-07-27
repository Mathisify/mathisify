from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('chapterone/', views.chapterone),
    path('about/', views.about),
    path('compandint/', views.compandint),
    path('chapterzero/', views.chapterzero),
    path('welcometoscratch/', views.welcometoscratch),
    path('search/', views.search),
]
