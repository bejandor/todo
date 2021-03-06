# Generated by Django 3.2.3 on 2021-05-17 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_rename_text_task31_text1'),
    ]

    operations = [
        migrations.CreateModel(
            name='Books_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tittle', models.CharField(max_length=40)),
                ('subtitle', models.CharField(max_length=25)),
                ('describtion', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('genre', models.CharField(max_length=40)),
                ('author', models.CharField(max_length=100)),
                ('year_of_issue', models.DecimalField(decimal_places=0, max_digits=4)),
                ('uploaded_at', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
