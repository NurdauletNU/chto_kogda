from django.http import JsonResponse


def index(request):
    return JsonResponse(data={'hello': 'world'})


def settings_get(request):
    print(request.headers)
    if request.headers.get("Authorization", '') != "Token = auth979":
        return JsonResponse(data={'error': 'invalid token'}, status=401)
    _data = {"temp_plan_high": -11, "temp_plan_down": -37}
    return JsonResponse(data={"data": _data}, status=200)
