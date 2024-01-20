# Generated by Django 5.0.1 on 2024-01-11 10:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("django_app", "0002_categoryitem_alter_item_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="item",
            name="category",
            field=models.ForeignKey(
                blank=True,
                default="",
                max_length=100,
                on_delete=django.db.models.deletion.CASCADE,
                to="django_app.categoryitem",
                verbose_name="Категория",
            ),
        ),
    ]