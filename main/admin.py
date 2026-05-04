from django.contrib import admin
from .models import Article, Profile


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at", "is_published")
    list_filter = ("is_published", "created_at")
    search_fields = ("title", "anons", "full_text")


admin.site.register(Profile)
