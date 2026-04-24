from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('quiz/', include('quiz.urls')),
    path('catalog/', include('catalog.urls')),
    path('map/', include('map.urls'))

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)