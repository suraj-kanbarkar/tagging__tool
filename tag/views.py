from django.http import JsonResponse
from django.shortcuts import render
from tag.models import TagData
from django.views.decorators.csrf import csrf_exempt
import csv

# Create your views here.


def read(request):
    items = TagData.objects.get(id=1)
    return render(request, 'base.html', context={'data': items.text})


@csrf_exempt
def tagged_text(request):
    if request.method == 'POST':
        data = request.POST
        print(data)
    return JsonResponse({'url': '/data/read/'}, status=200)
