from django.urls import path
from .views import query, result, ping, history

urlpatterns = [
    path('query/', query, name='query'), 
    path('result/', result, name='result'),
    path('ping/', ping, name='ping'),
    path('history/', history, name='history'),
]
