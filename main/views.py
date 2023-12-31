from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .forms import EstateForm


# Create your views here.
def index(request: HttpRequest):
    name = request.GET.get("name") or 'Charles'
    context = {
        'name': name,
        'title': 'Home Page'
    }
    return render(request,'index.html', context)


def greet(request: HttpRequest):
    name = request.GET.get("name") or 'Charles'
    return HttpResponse(f'Hello {name}')


def create_estate(request: HttpRequest):
    form = EstateForm()
    context = {
        'form': form
    }
    return render(request, context)
