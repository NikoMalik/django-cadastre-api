# cadastre_service/urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cadastre/', include('cadastre.urls')),  # Импортируем URL-паттерны из приложения cadastre
]
