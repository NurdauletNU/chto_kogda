import datetime

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
import re
from django_app import models

from django.urls import reverse


# Create your views here.


def home(request):
    categories = models.CategoryItem.objects.all()
    vips = models.Vip.objects.all().filter(expired__gt=datetime.datetime.now())
    return render(
        request, "HomePage.html", context={"categories": categories, "vips": vips}
    )


def search(request):
    if request.method == "POST":
        search = request.POST.get("search", "")
        items = models.Item.objects.all().filter(
            is_active=True, title__icontains=search
        )
        return render(request, "item_list.html", context={"items": items})


def item_list(request):
    # if not request.user.is_authenticated:
    #     return redirect(reverse("signin"))
    items = models.Item.objects.all().filter(is_active=True).order_by("price")
    return render(request, "item_list.html", context={"items": items})


def register(request):
    if request.method == "GET":
        return render(request, "RegisterPage.html")
    elif request.method == "POST":
        # print(request.POST, type(request.POST))
        username = str(request.POST["username"])
        password = str(request.POST["password"])
        email = str(request.POST["email"])
        password_regex = (
            r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
        )

        # не успешная регистрация
        if not re.match(password_regex, password):
            return render(
                request,
                "RegisterPage.html",
                context={"error": "password does not comply with the security policy"},
            )

        # ORM
        usr = User.objects.create(username=username, password=make_password(password))

        # вход в аккаунт
        # login()

        return redirect(reverse("item_list"))

        # authenticate()


def sign_in(request):
    if request.method == "GET":
        return render(request, "signin.html")
    elif request.method == "POST":
        username = str(request.POST["username"])
        password = str(request.POST["password"])

        user = authenticate(username=username, password=password)
        if user is None:
            return render(
                request,
                "signin.html",
                context={"error": "login and password do not match"},
            )
        login(request, user)
        return redirect(reverse("item_list"))


def sign_out(request):
    logout(request)
    return redirect(reverse("signin"))


def category_list(request):
    categories = models.CategoryItem.objects.all()
    return render(request, "category_list.html", context={"categories": categories})


def items(request, slug_name: str):
    cat = models.CategoryItem.objects.get(slug=slug_name)
    _items = models.Item.objects.all().filter(is_active=True, category=cat)
    return render(
        request,
        "item_list.html",
        context={"items": _items},
    )


def item(request, item_id: str):
    _item = models.Item.objects.get(id=int(item_id))
    return render(request, "item_detail.html", context={"item": _item})


from django.shortcuts import render, get_object_or_404
from .models import Product


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    comments = product.comments.all()
    new_comment = None

    if request.method == "POST":
        author = request.POST.get("author")
        text = request.POST.get("text")

        if author and text:
            new_comment = Comment(author=author, text=text, product=product)
            new_comment.save()

    return render(
        request,
        "product_detail.html",
        {
            "product": product,
            "comments": comments,
            "new_comment": new_comment,
        },
    )
