from django.shortcuts import render
from .models import Profession

def catalog(request):
    query = request.GET.get('q', '').strip()
    professions = Profession.objects.all()
    if query:
        professions = professions.filter(title__icontains=query)

    return render(request, 'catalog/catalog.html', {
        'professions': professions,
        'query': query,
    })


