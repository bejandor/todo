from django.db import models

#Создаем класс для будущих обьектов 
#Которые мы будем хранить в базе данных

class ToDo(models.Model):
    text = models.CharField(max_length=100) # Поле для хранения текста
    created_at  = models.DateField(auto_now_add = True) # Для хранения даты 
    is_done_task = models.BooleanField(default = False)
    is_favorite = models.BooleanField(default = False)



