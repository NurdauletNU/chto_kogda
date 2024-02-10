from django.urls import path
from django_app import views


urlpatterns = [
    path('', views.home, name='home'),
    path('api/', views.index),
    path('api/settings/get/', views.settings_get),
    path("api/settings/set/, views.settings_set"),
    # path('events/posts', views.post)
]
