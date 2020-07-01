# Generated by Django 3.0.5 on 2020-06-18 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0003_logentry_add_action_flag_choices'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=32, verbose_name='Марка')),
                ('model', models.CharField(max_length=32, verbose_name='Модель')),
                ('color', models.CharField(max_length=32, verbose_name='Цвет')),
                ('num', models.CharField(max_length=32, verbose_name='Гос. номер')),
            ],
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]
