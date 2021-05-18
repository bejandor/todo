from django.contrib import admin
from .models import ToDo,Task31,Books_data

# Register your models here.

# Для того чтобы наши поля(конструктор) появились в админ панели
# И по этому шаблону будет созданы обьекты и будут храниться в базе как целостные обьекты со 
# со своими методами
admin.site.register(ToDo) 
admin.site.register(Task31)
admin.site.register(Books_data)
