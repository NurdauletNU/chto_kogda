# Generated by Django 5.0.1 on 2024-01-11 10:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("django_app", "0003_alter_item_category"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="item",
            name="id",
        ),
        migrations.AlterField(
            model_name="item",
            name="title",
            field=models.CharField(
                blank=True,
                db_index=True,
                default="",
                max_length=250,
                primary_key=True,
                serialize=False,
                verbose_name="Наименование",
            ),
        ),
    ]