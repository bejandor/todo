from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .models import *


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

def add_todo(request):
    form = request.POST # 
    text1 = form["todo_text"] # Получаем переменную из формы
    todo = ToDo(text = text1)# Создаем объект ToDo у него есть атрибут(поле) text записываем text1
    todo.save() #Отправить запрос в базу для сохранения 
    return redirect(test)# После добавления перенаправление на страницу test

def add_book(request):
    form_book = request.POST # Получаем словарь

    title = form_book['title'] # Записываем в переменные по ключу
    subtitle = form_book['subtitle']
    genre = form_book['genre']
    author = form_book['author']
    year = form_book['year']
    descriptiton = form_book['description']
    price = form_book['price']

    books_obj = Books_data(
        # Создаем обьект  и передаем значения полученые по ключам в атрибуты класса - 
        #  - нового объекта
        title = title,
        subtitle = subtitle,
        genre = genre,
        author = author,
        year_of_issue = year,
        describtion = descriptiton,
        price = price
    )
    books_obj.save() # Сохраняем в базе 
    return redirect(books) # Перенаправляем на страницу books





        