from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, Category

def home(request):
    books = Book.objects.filter(status=Book.ACTIVE).order_by('-created_at')
    
    return render(request, 'book/home.html', {'books': books})

def detail(request, id):
    book = get_object_or_404(Book, id=id, status=Book.ACTIVE)
    context = {
        'book': book,
    }
    return render(request, 'book/detail_book.html', context)

def edit(request, id):
    return redirect('home')

def delete(request, id):
    return redirect('home')