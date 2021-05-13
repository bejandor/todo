from django.http.response import HttpResponse
from django.shortcuts import render
# Create your views here.

def homepage(request):
    return HttpResponse("Hello world")


def test(request):
    return render(request,"test.html")

def second(request):
    return HttpResponse("Test2 page")

def third(request):
    return HttpResponse("This is page test3")