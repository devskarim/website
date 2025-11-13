from django.urls import path
from .views import home, add_book, book_list

urlpatterns = [
    path('', home, name='home'),
    path('add/', add_book, name='add_book'),
    path('books/', book_list, name='book_list'),
]
