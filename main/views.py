from django.shortcuts import get_object_or_404, render
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


def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id, is_published=True)
    return render(request, 'main/article_detail.html', {
        'article': article,
    })
