from django.urls import path
from .views import SearchPage

urlpatterns = [
    path('search/', SearchPage, name='search'),
    # Other URL patterns in your project
]
