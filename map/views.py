from django.shortcuts import render
from .models import University

def map(request):
    universities = University.objects.prefetch_related('specialty_set').all()
    return render(request, 'map/map.html', {'universities': universities})

