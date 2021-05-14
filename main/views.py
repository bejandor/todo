from django.http.response import HttpResponse
from django.shortcuts import render
# Create your views here.

def homepage(request):
    return render(request, "index.html") #Метод который отображает наш index файл


def test(request):
    return render(request, "test.html") #Метод который отображает наш test файл
