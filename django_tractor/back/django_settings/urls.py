import json

from django.http import JsonResponse
from django.urls import path
from django.views.decorators.csrf import csrf_exempt


def api(request):
    return JsonResponse(data={'success': 'ok'}, status=200)


@csrf_exempt
def communicator(request):
    if request.method != 'POST':
        return JsonResponse(data={'error': 'method not supported'}, status=500)
    # print(request.body)
    body: bytes = request.body
    data = json.loads(body)
    messages = data.get('messages', [])
    return JsonResponse(data={'success': 'ok'}, status=201)


urlpatterns = [
    path('api/', api),
    path('api/communicator', communicator)
]
