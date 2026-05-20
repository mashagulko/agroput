from django.contrib import admin
from .models import Test, Question, AnswerVariant, QuestionProfession


class QuestionProfessionInline(admin.TabularInline):
    model = QuestionProfession
    extra = 1


class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ("title", "is_active")
    search_fields = ("title",)
    list_filter = ("is_active",)
    inlines = [QuestionInline]


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("text", "test", "order")
    list_filter = ("test",)
    search_fields = ("text",)
    ordering = ("order",)
    inlines = [QuestionProfessionInline]


@admin.register(AnswerVariant)
class AnswerVariantAdmin(admin.ModelAdmin):
    list_display = ("text", "points", "order")
    ordering = ("order",)


@admin.register(QuestionProfession)
class QuestionProfessionAdmin(admin.ModelAdmin):
    list_display = ("question", "profession")
    list_filter = ("profession",)
    search_fields = ("question__text", "profession__title")