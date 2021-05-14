from django.contrib import admin
from .models import ToDo

# Register your models here.

# Для того чтобы наши поля(конструктор) появились в админ панели
# И по этому шаблону будет созданы обьекты и будут храниться в базе как целостные обьекты со 
# Со своими методами
admin.site.register(ToDo) 
