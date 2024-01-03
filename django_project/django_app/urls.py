from django.urls import path
from django_app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('item_list/', views.home, name='item_list'),
    path('register/', views.register, name='register'),
    path('signin', views.sign_in, name='signin'),
    path('sign_out', views.sign_out, name='sign_out'),
    path('item_list', views.item_list, name='item_list')

]
