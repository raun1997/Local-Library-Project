from django.shortcuts import render
from .models import Book, Author
from django.utils.timezone import now

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()

    # Available books (status = 'a')
    # num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    context = {
        'num_books': num_books,
        'num_authors': num_authors,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

def books(request):
    books = Book.objects.all()
    time = now()
    context = {
        "books": books,
        "time" : time,
    }
    return render(request, "catalog/books.html", context=context)

def book_details(request, pk):
    book = Book.objects.get(pk=pk)
    context = {
        "book": book
    }
    return render(request, "catalog/book_details.html", context=context)


def authors(request):
    authors = Author.objects.all()
    context = {
        "authors": authors
    }
    return render(request, "catalog/authors.html", context=context)

def author_details(request, pk):
    author = Author.objects.get(pk=pk)
    books = Book.objects.filter(author=author).values()
    context = {
        "author": author,
        "books":books
    }
    return render(request, "catalog/author_details.html", context=context)
