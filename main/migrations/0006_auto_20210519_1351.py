# Generated by Django 3.2.3 on 2021-05-19 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_todo_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books_data',
            name='subtitle',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='books_data',
            name='tittle',
            field=models.CharField(max_length=100),
        ),
    ]
