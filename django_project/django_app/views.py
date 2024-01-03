from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
import re
from django_app import models

from django.urls import reverse


# Create your views here.


def home(request):
    return render(request, 'HomePage.html')


def item_list(request):
    if not request.user.is_authenticated:
        return redirect(reverse('signin'))

    # items = models.Item.objects.all.filter(is_active=True)
    return render(request, 'item_list.html')



def register(request):
    if request.method == 'GET':
        return render(request, 'RegisterPage.html')
    elif request.method == 'POST':
        # print(request.POST, type(request.POST))
        username = str(request.POST['username'])
        password = str(request.POST['password'])
        email = str(request.POST['email'])
        password_regex = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"

        # не успешная регистрация
        if not re.match(password_regex, password):
            return render(request, 'RegisterPage.html',
                          context={'error': 'password does not comply with the security policy'})

        # ORM
        usr = User.objects.create(username=username, password=make_password(password))

        # вход в аккаунт
        # login()

        return redirect(reverse('item_list'))

        # authenticate()


def sign_in(request):
    if request.method == 'GET':
        return render(request, 'signin.html')
    elif request.method == 'POST':
        username = str(request.POST['username'])
        password = str(request.POST['password'])

        user = authenticate(username=username, password=password)
        if user is None:
            return render(request, 'signin.html', context={'error': 'login and password do not match'})
        login(request, user)
        return redirect(reverse('item_list'))


def sign_out(request):
    logout(request)
    return redirect(reverse('signin'))
