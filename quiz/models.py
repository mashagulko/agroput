from django.db import models
from catalog.models import Profession


class Test(models.Model):
    title = models.CharField("Название теста", max_length=255)
    description = models.TextField("Описание", blank=True, null=True)
    is_active = models.BooleanField("Активен", default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Тест"
        verbose_name_plural = "Тесты"


class Question(models.Model):
    test = models.ForeignKey(
        Test,
        on_delete=models.CASCADE,
        related_name="questions",
        verbose_name="Тест"
    )
    text = models.TextField("Текст вопроса")
    order = models.PositiveIntegerField("Порядок", default=0)

    professions = models.ManyToManyField(
        Profession,
        through="QuestionProfession",
        related_name="quiz_questions",
        verbose_name="Профессии"
    )

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"
        ordering = ["order"]


class AnswerVariant(models.Model):
    text = models.CharField("Вариант ответа", max_length=100)
    points = models.PositiveIntegerField("Баллы")
    order = models.PositiveIntegerField("Порядок", default=0)

    def __str__(self):
        return f"{self.text} — {self.points}"

    class Meta:
        verbose_name = "Вариант ответа"
        verbose_name_plural = "Варианты ответов"
        ordering = ["order"]


class QuestionProfession(models.Model):
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name="profession_links",
        verbose_name="Вопрос"
    )
    profession = models.ForeignKey(
        Profession,
        on_delete=models.CASCADE,
        related_name="question_links",
        verbose_name="Профессия"
    )

    def __str__(self):
        return f"{self.question} → {self.profession}"

    class Meta:
        verbose_name = "Связь вопроса с профессией"
        verbose_name_plural = "Связи вопросов с профессиями"
        unique_together = ("question", "profession")