# Generated by Django 5.0 on 2024-01-07 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, db_index=True, default='', max_length=150, verbose_name='Название')),
                ('author', models.CharField(blank=True, db_index=True, default='', max_length=150, verbose_name='Автор')),
                ('price', models.PositiveIntegerField(blank=True, default='', verbose_name='Цена')),
                ('quantity', models.PositiveIntegerField(blank=True, default='', verbose_name='Количетсво')),
            ],
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
