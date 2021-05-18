from django.http.response import HttpResponse
from django.shortcuts import render
from .models import ToDo,Task31,Books_data

# Create your views here.

def homepage(request):
    return render(request, "index.html") #Метод который отображает наш index файл


def test(request):
    # Получаем все наши записи из базы данных и формируем список из объектов
    todo_list = ToDo.objects.all() # Записываем все это в todo_list

    return render(request, "test.html",{"todo_list":todo_list})
    #Передаем todo_list на страницу в виде словаря {"Значение":ключь}

#Создаем функцию для отображения в views наш html примеры с jinja
def test2_index(request):
    return render(request, "main/index.html") 

def test2_about(request):
    return render(request, "main/about.html")


def test_task31(request):
    #Получаем обьект из созданных моделей
    task31_list = Task31.objects.all()
    return render(request, "test_task31.html",{"task31_list":task31_list})

def books(request):
    books_data_list = Books_data.objects.all()
    return render(request, "books.html",{"books_data_list":books_data_list})    
        