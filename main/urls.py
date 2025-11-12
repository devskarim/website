from django.urls import path
from .views import home, add_book

urlpatterns = [
	path('', home),
	path('add/', add_book, name='add_book')
]