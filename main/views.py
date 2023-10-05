from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


# Create your views here.
def index(request: HttpRequest):
    name = request.GET.get("name") or 'Charles'
    context = {
        'name': name
    }
    return render(request,'index.html', context)


def greet(request: HttpRequest):
    name = request.GET.get("name") or 'Charles'
    return HttpResponse(f'Hello {name}')
