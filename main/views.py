from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html')

def catalog(request):
    return render(request, 'main/catalog.html')

def map(request):
    return render(request, 'main/map.html')