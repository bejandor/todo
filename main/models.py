from django.db import models
'''Создание этого класса позволит нам в админ панеле django создавть объекты которые будут
храниться в базе данных в виде объектов.Будем подставлять их значения при помощи
шаблонизатора jinja , в html странице.
'''
class ToDo(models.Model):
    text = models.CharField(max_length=100) # Поле для хранения текста
    created_at  = models.DateField(auto_now_add = True) # Для хранения даты будет добавлятся автоматически
    is_done_task = models.BooleanField(default = False)
    is_favorite = models.BooleanField(default = False)

class Task31(models.Model):
    text1 = models.CharField(max_length=100)

