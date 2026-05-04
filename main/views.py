from django.shortcuts import render
from .models import Article

def index(request):
    articles = Article.objects.filter(is_published=True)
    return render(request, 'main/index.html', {'articles': articles})

