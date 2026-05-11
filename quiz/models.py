from django.db import models
from django.contrib.auth.models import User
from catalog.models import Profession


class Test(models.Model):
    title = models.CharField("Название теста", max_length=200)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Тест"
        verbose_name_plural = "Тесты"


class Question(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, verbose_name="Тест")
    text = models.TextField("Вопрос")
    professions = models.ManyToManyField(Profession, verbose_name="Профессии")

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name="Вопрос")
    text = models.CharField("Ответ", max_length=200)
    score = models.IntegerField("Баллы")

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Ответ"
        verbose_name_plural = "Ответы"


class TestResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Пользователь")
    profession = models.ForeignKey(Profession, on_delete=models.CASCADE, verbose_name="Профессия")
    score = models.IntegerField("Баллы")

    def __str__(self):
        return f"{self.user} - {self.profession}"

    class Meta:
        verbose_name = "Результат теста"
        verbose_name_plural = "Результаты тестов"