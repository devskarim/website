from django.shortcuts import render
from .models import Book
from .forms import BookForm 

def home(request): 
	form = BookForm()
	book = Book.objects.all()

	context  = {
		"form": form,
		"book": book
	}
	return render(request, 'index.html', context=context)


def add_book(request): 
	form = BookForm()
	book = Book.objects.all()

	context  = {
		"form": form,
		"book": book
	}
	return render(request, 'add.html', context=context)