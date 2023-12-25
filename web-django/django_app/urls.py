"""
django_app/urls.py - Маршрутизация на уровне приложении
"""

from django.urls import path
from django_app import views


urlpatterns = [
    # домашняя страница
    path("", views.home, name="home"),
    path("letter", views.letter, name="letter"),

]