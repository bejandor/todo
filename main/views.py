from django.http.response import HttpResponse
from django.shortcuts import render
from .models import ToDo #Импортируем наш класс ToDo
# Create your views here.

def homepage(request):
    return render(request, "index.html") #Метод который отображает наш index файл


def test(request):
    todo_list = ToDo.objects.all()
    return render(request, "test.html",{"todo_list":todo_list}) #Метод который отображает наш test файл
