from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils import timezone


# Create your models here.
class CategoryItem(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(
        verbose_name="Наименование",
        db_index=True,
        primary_key=False,
        unique=True,
        editable=True,
        blank=True,
        null=False,
        default="",
        max_length=250,
    )

    slug = models.SlugField(
        verbose_name="Ссылка",
        db_index=True,
        primary_key=False,
        unique=True,
        editable=True,
        blank=True,
        null=False,
        default="",
        max_length=250,
    )
    objects = models.Manager()

    class Meta:
        app_label = "django_app"
        ordering = ("-title",)
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return f"<CategoryItem {self.title} = {self.slug} />"


class Item(models.Model):
    id = models.AutoField
    title = models.CharField(
        verbose_name="Наименование",
        db_index=True,
        primary_key=True,
        unique=False,
        editable=True,
        blank=True,
        null=False,
        default="",
        max_length=250,
    )

    description = models.TextField(
        verbose_name="Описание",
        db_index=False,
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=False,
        default="",
    )

    price = models.PositiveIntegerField(
        verbose_name="Цена",
        db_index=False,
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=False,
        default="",
    )

    # category = models.CharField(
    #     verbose_name="Категория",
    #     db_index=True,  # индексы используются в фильтрации
    #     primary_key=False,
    #     unique=False,
    #     editable=True,
    #     blank=True,
    #     null=False,
    #     default="",
    #     max_length=100,
    # )

    category = models.ForeignKey(  # O2M
        verbose_name="Категория",
        db_index=True,  # индексы используются в фильтрации
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=False,
        default="",
        max_length=100,
        to=CategoryItem,
        on_delete=models.CASCADE,  # CASCADE - удаление
    )
    avatar = models.ImageField(
        verbose_name="Аватар",
        validators=[FileExtensionValidator(["jpg", "jpeg", "png", "bmp"])],
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default=None,
        upload_to="item/avatars",
    )

    file = models.FileField(
        verbose_name="Инструкция",
        validators=[FileExtensionValidator(["xlsx", "docx", "pdf"])],
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default=None,
        upload_to="item/files",
    )

    is_active = models.BooleanField(
        verbose_name="Активность",
        null=False,
        default=True,
    )
    objects = models.Manager()

    class Meta:
        app_label = "django_app"
        ordering = ("is_active", "-title")
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        if self.is_active:
            act = "активен"
        else:
            act = "продано"
        return f"<Item {self.title} | {act} | {self.description[:30]} />"


class Vip(models.Model):
    id = models.AutoField
    article = models.OneToOneField(  # O2O
        verbose_name="Объявление",
        db_index=True,  # индексы используются в фильтрации
        primary_key=False,
        editable=True,
        blank=True,
        null=False,
        default="",
        max_length=100,
        to=Item,
        on_delete=models.CASCADE,  # CASCADE - удаление
    )
    priority = models.IntegerField(
        verbose_name="Приоритет",
        db_index=True,
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=False,
        default=1,
    )

    expired = models.DateTimeField(
        verbose_name="дата и время истичения",
        db_index=True,
        primary_key=True,
        unique=False,
        editable=True,
        blank=True,
        null=False,
        default=timezone.now,
        max_length=250,
    )

    objects = models.Manager()

    class Meta:
        app_label = "django_app"
        ordering = ("priority", "expired")
        verbose_name = "Vip объявление"
        verbose_name_plural = "Vip объявлении"

    def __str__(self):
        return f"<Vip {self.article} | {self.priority} />"


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    objects = models.Manager()


class Room(models.Model):
    name = models.CharField(
        verbose_name="Наименование",
        db_index=True,
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=False,
        default="",
        max_length=250,
    )

    slug = models.SlugField(
        verbose_name="Ссылка",
        db_index=True,
        primary_key=False,
        unique=True,
        editable=True,
        blank=True,
        null=False,
        default="",
        max_length=250,
    )
    objects = models.Manager()

    class Meta:
        app_label = "django_app"
        ordering = ("-slug", "-name")

    def __str__(self):
        return f"<Room {self.name} {self.slug} | {self.slug} ({self.id})/>"


class Message(models.Model):
    user = models.ForeignKey(
        verbose_name="Автор",
        db_index=True,
        primary_key=False,
        editable=True,
        blank=True,
        null=False,
        default="",
        max_length=100,
        #
        to=User,
        on_delete=models.CASCADE,
    )
    room = models.ForeignKey(
        verbose_name="Комната",
        db_index=True,
        primary_key=False,
        editable=True,
        blank=True,
        null=False,
        default="",
        max_length=100,
        #
        to=Room,
        on_delete=models.CASCADE,
    )
    content = models.TextField(
        verbose_name="Текст сообщения",
        db_index=False,
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=False,
        default="",
    )
    date_added = models.DateTimeField(
        verbose_name="дата и время добавления",
        db_index=True,
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=False,
        default=timezone.now,
        max_length=300,
    )
    objects = models.Manager()

    class Meta:
        app_label = "django_app"
        ordering = ("-date_added", "-room")

    def __str__(self):
        return f"<Message {self.room.name} {self.user.username} {self.content[:30]} ({self.id})/>"
