from django.http import HttpResponse
from django.shortcuts import HttpResponse, render


# Create your views here.
def index(request):
    return render(request, "hello/index.html")


def james(request):
    return HttpResponse("<h1> Hi James!</h1>")


def peter(request):
    return HttpResponse("<h3>Hi Peter!</h3>")


def greet(request, name):
    return render(request, "hello/greet.html", {"name": name.capitalize()})
