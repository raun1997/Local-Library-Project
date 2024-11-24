from django.urls import path
from . import views    # from current directory, import views

urlpatterns = [
    path('', views.index, name="index"),
    path('books/', views.books, name="books"),
]
