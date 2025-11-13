from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm 

def home(request): 
    form = BookForm()
    books = Book.objects.all()
    context  = {
        "form": form,
        "books": books
    }
    return render(request, 'index.html', context=context)


def add_book(request): 
    form = BookForm()
    books = Book.objects.all()

    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            Book.objects.create(
                title=form.cleaned_data.get('title'),
                author=form.cleaned_data.get('author'),
                desc=form.cleaned_data.get('desc'),
                price=form.cleaned_data.get('price')
            )
            return redirect('/') 

    context = {
        "form": form,
        "books": books
    }
    return render(request, 'add.html', context=context)

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'book': books})
