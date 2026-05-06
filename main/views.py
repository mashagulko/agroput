from django.shortcuts import render
from .models import Article
from catalog.models import Profession
from map.models import University

def index(request):
    articles = Article.objects.filter(is_published=True)
    professions = Profession.objects.all()
    universities = University.objects.all()
    context = {
        'articles': articles,
        'professions': professions,
        'universities': universities,
    }
    return render(request, 'main/index.html', context)

