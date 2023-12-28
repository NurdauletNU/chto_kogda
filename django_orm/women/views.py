from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from women import models
from women.models import Women

def index(request):
    return HttpResponse('Страница приложения women')


def categories(request, catid):
    if request.GET:
        print(request.GET)
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>{catid}</p>")


def archive(request, year):
    if int(year)>2023:
        return redirect('home', permanent=True)
    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


def create_woman(request):
    w1: Women = Women.objects.create(title="Анджелина Джоли",
        content='Биография Анджелина Джоли')
    print(w1)
    return HttpResponseRedirect('/create_women/')


def delete_woman(request, woman_id):
    woman = get_object_or_404(Women, pk=woman_id)
    woman.delete()
    return HttpResponseRedirect('/delete_women/')









