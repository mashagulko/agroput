from django.db import models


class Profession(models.Model):
    title = models.CharField("Название профессии", max_length=200)
    description = models.TextField("Описание", null=True, blank=True)
    salary = models.IntegerField("Зарплата", null=True, blank=True)
    link = models.URLField("Ссылка", null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Профессия"
        verbose_name_plural = "Профессии"