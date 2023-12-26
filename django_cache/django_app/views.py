from django.http import HttpResponse
from django.core.cache import caches, cache
import random
# Create your views here.


RamCache = caches["default"]
DatabaseCache = caches["special"]


def index(request):
    data = cache.get('cached_data')
    if data is None:
        data = random.randint(1, 100000)
        cache.set('cached_data', data, timeout=10)
    print(data)
    return HttpResponse(" Здорово! ")





