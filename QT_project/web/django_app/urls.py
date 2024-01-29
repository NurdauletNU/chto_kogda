from django.urls import path
from django_app import views

urlpatterns = [
    path('', views.index),
    path('settings/get/', views.settings_get),
    # path('events/posts', views.post)
]
