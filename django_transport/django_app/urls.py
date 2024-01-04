from django.urls import path
from django_app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('prices/', views.prices, name='prices'),
    path('products/', views.products, name='products')
]
