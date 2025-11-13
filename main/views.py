from django.shortcuts import render,redirect
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

	if request.method == "POST": 
		data = BookForm(request.POST)
		if data.is_valid():
			Book.objects.create(
				title = data.cleaned_data.get('title'),
				author = data.cleaned_data.get('author'),
				desc = data.cleaned_data.get('desc'),
				price = data.cleaned_data.get('price')
			)
			return redirect('/')
		else: 
			form = Book.objects.all()

	
	context  = {
		"form": form,
		"book": book
	}
	return render(request, 'add.html', context=context)