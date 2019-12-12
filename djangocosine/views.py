from django.shortcuts import render
import json
from django.http import HttpResponse
from django.http import JsonResponse
import math
from collections import Counter

from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def index(request):
    l1 = request.POST['text1'].split()
    l2 = request.POST['text2'].split()
    v1, v2 = build_vector(l1, l2)
    result = cosim(v1, v2)

    return HttpResponse(result)

def build_vector(iterable1, iterable2):
    counter1 = Counter(iterable1)
    counter2 = Counter(iterable2)
    all_items = set(counter1.keys()).union(set(counter2.keys()))
    vector1 = [counter1[k] for k in all_items]
    vector2 = [counter2[k] for k in all_items]
    return vector1, vector2

def cosim(v1, v2):
    dot_product = sum(n1 * n2 for n1, n2 in zip(v1, v2) )
    magnitude1 = math.sqrt(sum(n ** 2 for n in v1))
    magnitude2 = math.sqrt(sum(n ** 2 for n in v2))
    return dot_product / (magnitude1 * magnitude2)