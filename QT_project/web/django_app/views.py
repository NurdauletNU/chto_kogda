from django.http import JsonResponse
from django.shortcuts import render

from web.django_app import utils


def index(request):
    return JsonResponse(data={'hello': 'world'})


def settings_get(request):
    print(request.headers)
    if request.headers.get("Authorization", "") != "Token=auth979":
        return JsonResponse(data={'error': 'invalid token'}, status=401)
    _data = {"temp_plan_high": -11, "temp_plan_down": -30}
    return JsonResponse(data={"data": _data}, status=200)


def home(request):
    _rows = utils.Sql.sql_execute(
        _query="""SELECT key,value FROM params; """,
        _kwargs={},
        _source='local_settings_db',
    )
    _dict = [{'key': str(x[0]), 'value': str(x[1])} for x in _rows]
    _params = {}
    for i in _dict:
        _params[i['key']] = i['value']
        return render(request, 'home.html', context={'params': _params})
