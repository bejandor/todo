from django.db import models
from django.db.models.fields import DecimalField
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
    text1 = models.CharField(max_length = 100)



class Books_data(models.Model):
    tittle = models.CharField(max_length =  40)
    subtitle = models.CharField(max_length =  25)
    describtion = models.CharField(max_length = 200)
    price = models.DecimalField(max_digits= 7 ,decimal_places = 2)
    genre = models.CharField(max_length = 40)
    author = models.CharField(max_length = 100)
    year_of_issue = models.DecimalField(max_digits = 4,decimal_places = 0)
    uploaded_at = models.DateField(auto_now_add = True)

