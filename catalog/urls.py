from django.urls import path
from . import views    # from current directory, import views

urlpatterns = [
    path('', views.index, name="index"),
    path('books/', views.books, name="books"),
    path('book/<int:pk>/', views.book_details, name="book-detail"),
    path('authors/', views.authors, name="authors"),
    path('author/<int:pk>/', views.author_details, name="author-detail"),
]
