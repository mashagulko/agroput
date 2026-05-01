from django.db import models
from catalog.models import Profession


class University(models.Model):
    name = models.CharField("Название университета", max_length=200)
    address = models.CharField("Адрес", max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Университет"
        verbose_name_plural = "Университеты"


class Specialty(models.Model):
    name = models.CharField("Название специальности", max_length=200)
    description = models.TextField("Описание")

    university = models.ForeignKey(
        University,
        on_delete=models.CASCADE,
        verbose_name="Университет"
    )
    professions = models.ManyToManyField(
        Profession,
        verbose_name="Профессии"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Специальность"
        verbose_name_plural = "Специальности"