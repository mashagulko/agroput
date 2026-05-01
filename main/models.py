from django.db import models
from django.contrib.auth.models import User


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