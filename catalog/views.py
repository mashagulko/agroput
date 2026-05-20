from django.shortcuts import get_object_or_404, render
from .models import Profession


def catalog(request):
    professions = Profession.objects.all()
    return render(request, 'catalog/catalog.html', {'professions': professions})


def profession_detail(request, pk):
    profession = get_object_or_404(Profession, pk=pk)
    return render(request, 'catalog/profession_detail.html', {'profession': profession})
