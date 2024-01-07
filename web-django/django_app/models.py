from django.core.validators import EmailValidator
from django.db import models


# Create your models here.

class Book(models.Model):

    title = models.CharField(
        verbose_name='Название',
        db_index=True,
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=False,
        default='',
        max_length=150,
    )
    author = models.CharField(
        verbose_name='Автор',
        db_index=True,
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=False,
        default='',
        max_length=150,
    )
    price = models.PositiveIntegerField(
        verbose_name='Цена',
        db_index=False,
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=False,
        default='',
    )
    quantity = models.PositiveIntegerField(
        verbose_name='Количетсво',
        db_index=False,
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=False,
        default='',
    )


class Meta:
    app_label = 'django_app'
    ordering = ('title',)
    verbose_name = 'Книги'
    verbose_name_plural = 'Товары'


def __str__(self):
    if self.quantity > 0:
        quan='есть книжки'
    else:
        quan='нет книжек'
    return f'<BOOK {self.title}| ({self.author}) {quan} {self.price}>'

