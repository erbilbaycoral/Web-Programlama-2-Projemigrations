from django.shortcuts import render, get_object_or_404
from .models import Book

def index(request):
    # Veritabanındaki tüm kitapları çekip sayfaya gönderiyoruz
    books = Book.objects.all()
    return render(request, 'catalog/index.html', {'books': books})

def book_detail(request, pk):
    # Seçilen kitabın detaylarını çekiyoruz
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'catalog/book_detail.html', {'book': book})