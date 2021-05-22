"""TODO URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", homepage, name="home"),
    path("test/", test, name="test"),
    path('test2_index/',test2_index,name="test2_index"),
    path("test2_about/",test2_about, name="test2_about"),
    path("test_task31/",test_task31, name="test_task31"),
    path("books", books, name="books"),#2 объязательных праметра  ("Запрошенный адрес URL/", и функция которая )
    # ее обрабатывает запрос по этому адресу, можно указать имя = "маршрута")
    path("add-todo/", add_todo, name="add-todo"),
    path("add-book/", add_book, name="add-book"),
    path("delete-todo/<id>/", delete_todo, name="delete-todo"),
    path("mark-todo/<id>/",mark_todo,name="mark-todo"),
    path("unmark-todo/<id>/",unmark_todo,name="unmark-todo"),
    

    ] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT) \
  + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
  # Прописали 2 строки кода которые нужны для корректной работы статичных фалов а
  # так же для медиа файлов
  
