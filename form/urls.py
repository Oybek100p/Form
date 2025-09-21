from  django.urls import path
from . import views

urlpatterns = [
    path('authors/', views.AuthorList, name='authors'),
    path('author_add/', views.AuthorForm, name='author_add'),
    path('author_delete/<int:id>/', views.AuthorDelete, name='author_delete'),
    path('author_update/<int:id>/', views.AuthorUpdate, name='author_update'),


    path('books/', views.BookList, name='books'),
    path('book_add/', views.BookForm, name='book_add'),
    path('book_delete/<int:id>/', views.BookDelete, name='book_delete'),
    path('book_update/<int:id>/', views.BookUpdate, name='book_update'),

    path('', views.logo, name='logo'),
]