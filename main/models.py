from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    title = models.CharField("Заголовок", max_length=200)
    anons = models.CharField("Краткое описание", max_length=250)
    full_text = models.TextField("Текст статьи")
    created_at = models.DateTimeField("Дата публикации", auto_now_add=True)
    is_published = models.BooleanField("Опубликовано", default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
        ordering = ["-created_at"]


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name="Пользователь"
    )
    full_name = models.CharField("ФИО", max_length=200)
    age = models.IntegerField("Возраст")

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"
