# Generated by Django 5.0.1 on 2024-01-23 18:09

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("django_app", "0012_alter_item_author"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Profile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "patronymic",
                    models.CharField(
                        blank=True,
                        default="",
                        max_length=200,
                        null=True,
                        verbose_name="Отчество",
                    ),
                ),
                (
                    "avatar",
                    models.ImageField(
                        blank=True,
                        default=None,
                        null=True,
                        upload_to="avatars/",
                        validators=[
                            django.core.validators.FileExtensionValidator(
                                ["jpg", "jpeg", "png"]
                            )
                        ],
                        verbose_name="Аватар",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        blank=True,
                        default=None,
                        max_length=300,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="profile",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Автор",
                    ),
                ),
            ],
            options={
                "ordering": ("-user",),
            },
        ),
    ]
