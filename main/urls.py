from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('chapterone/', views.chapterone),
    path('chaptertwo/', views.chaptertwo),
]
