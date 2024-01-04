from django.shortcuts import render
from django_app import models
import random
from django_app.models import Price
from django.core.paginator import Paginator


# Create your views here.
def home(request):
    return render(request, "home.html")


def prices(request):
    data = [
        {
            "id": 1,
            "title": "Доставка фруктов",
            "description": "безопасно и без форс мажора",
            "price": 10000,
        },
        {
            "id": 2,
            "title": "Доставка пиццы",
            "description": "безопасно и без форс мажора",
            "price": 5000,
        },
        {
            "id": 3,
            "title": "Доставка пирога",
            "description": "безопасно и без форс мажора",
            "price": 7500,
        },
    ]
    return render(request, "prices.html", context={"prices": data})


def products(request):
    data = [
        {
            "id": 1,
            "title": "Доставка фруктов",
            "description": "безопасно и без форс мажора",
            "price": 10000,
        },
        {
            "id": 2,
            "title": "Доставка пиццы",
            "description": "безопасно и без форс мажора",
            "price": 5000,
        },
        {
            "id": 3,
            "title": "Доставка пирога",
            "description": "безопасно и без форс мажора",
            "price": 7500,
        },
        {
            "id": 4,
            "title": "Доставка фруктов",
            "description": "безопасно и без форс мажора",
            "price": 10000,
        },
        {
            "id": 5,
            "title": "Доставка пиццы",
            "description": "безопасно и без форс мажора",
            "price": 5000,
        },
        {
            "id": 6,
            "title": "Доставка пирога",
            "description": "безопасно и без форс мажора",
            "price": 7500,
        },
        {
            "id": 7,
            "title": "Доставка фруктов",
            "description": "безопасно и без форс мажора",
            "price": 10000,
        },
        {
            "id": 8,
            "title": "Доставка пиццы",
            "description": "безопасно и без форс мажора",
            "price": 5000,
        },
        {
            "id": 9,
            "title": "Доставка пирога",
            "description": "безопасно и без форс мажора",
            "price": 7500,
        },
        {
            "id": 10,
            "title": "Доставка фруктов",
            "description": "безопасно и без форс мажора",
            "price": 10000,
        },
        {
            "id": 11,
            "title": "Доставка пиццы",
            "description": "безопасно и без форс мажора",
            "price": 5000,
        },
        {
            "id": 12,
            "title": "Доставка пирога",
            "description": "безопасно и без форс мажора",
            "price": 7500,
        },
        {
            "id": 13,
            "title": "Доставка фруктов",
            "description": "безопасно и без форс мажора",
            "price": 10000,
        },
        {
            "id": 14,
            "title": "Доставка пиццы",
            "description": "безопасно и без форс мажора",
            "price": 5000,
        },
        {
            "id": 15,
            "title": "Доставка пирога",
            "description": "безопасно и без форс мажора",
            "price": 7500,
        },
        {
            "id": 16,
            "title": "Доставка фруктов",
            "description": "безопасно и без форс мажора",
            "price": 10000,
        },
        {
            "id": 17,
            "title": "Доставка пиццы",
            "description": "безопасно и без форс мажора",
            "price": 5000,
        },
        {
            "id": 18,
            "title": "Доставка пирога",
            "description": "безопасно и без форс мажора",
            "price": 7500,
        },
        {
            "id": 19,
            "title": "Доставка фруктов",
            "description": "безопасно и без форс мажора",
            "price": 10000,
        },
        {
            "id": 20,
            "title": "Доставка пиццы",
            "description": "безопасно и без форс мажора",
            "price": 5000,
        },
        {
            "id": 21,
            "title": "Доставка пирога",
            "description": "безопасно и без форс мажора",
            "price": 7500,
        },
        {
            "id": 22,
            "title": "Доставка фруктов",
            "description": "безопасно и без форс мажора",
            "price": 10000,
        },
        {
            "id": 23,
            "title": "Доставка пиццы",
            "description": "безопасно и без форс мажора",
            "price": 5000,
        },
        {
            "id": 24,
            "title": "Доставка пирога",
            "description": "безопасно и без форс мажора",
            "price": 7500,
        },
        {
            "id": 25,
            "title": "Доставка фруктов",
            "description": "безопасно и без форс мажора",
            "price": 10000,
        },
        {
            "id": 26,
            "title": "Доставка пиццы",
            "description": "безопасно и без форс мажора",
            "price": 5000,
        },
        {
            "id": 27,
            "title": "Доставка пирога",
            "description": "безопасно и без форс мажора",
            "price": 7500,
        },
        {
            "id": 28,
            "title": "Доставка фруктов",
            "description": "безопасно и без форс мажора",
            "price": 10000,
        },
        {
            "id": 29,
            "title": "Доставка пиццы",
            "description": "безопасно и без форс мажора",
            "price": 5000,
        },
        {
            "id": 30,
            "title": "Доставка пирога",
            "description": "безопасно и без форс мажора",
            "price": 7500,
        },
    ]

    sel_page = request.GET.get("page", default=1)

    page_objs = Paginator(data, 8)
    page_obj = page_objs.page(sel_page)

    # def paginate(obj:list, selected_page: int=1,limit: int=7):
    #     pass
    return render(request, "products.html", context={"page_obj": page_obj})
