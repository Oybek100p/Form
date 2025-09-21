from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from . import forms
from . import models

def AuthorList(req):
    authors = models.Author.objects.all()
    context = {
        'authors':authors
    }
    return render(req, 'author-list.html', context)

def AuthorForm(req):
    if req.method == "POST":
        form = forms.AuthorForm(req.POST)
        if form.is_valid():
            models.Author.objects.create(
            name = form.cleaned_data['name'],
            surname = form.cleaned_data['surname'],
            bio = form.cleaned_data['bio']
            )
            messages.success(req, "Form added")
            return redirect( 'authors')
    else:
        form = forms.AuthorForm()
    return render(req, 'form_author.html', {'form':form})

def AuthorDelete(req, id):
    author = get_object_or_404(models.Author, id = id)
    if req.method == "POST":
        author.delete()
        messages.success(req, 'Finish')
        return redirect('authors')
    return render(req, 'author_delete.html', {'author':author})

def AuthorUpdate(req, id):
    author = get_object_or_404(models.Author, id = id)
    if req.method == "POST":
        form = forms.AuthorForm(req.POST )
        if form.is_valid():
            form.save()
        return redirect('authors')
    else:
        form = forms.AuthorForm()
    return render(req, 'author_update.html', {'form':form})

#v#v#v#v#v#v#v#v#v#v#v#v#v#v#v#v#v#v#v#v#v#v#v#v#v#v#v#v#v#v#v#v#v#v#v#v#v#v#v#v#v#v#v#v#v#v#v#v#v#v#v#v#v#v#v#v#v#v#v#v#v#v#v#v#v#v#v#v#v#v#v#v#v#v#v#v#v#v#v#v#v#v#v#v#v

def BookList(req):
    books = models.Book.objects.all()
    context = {
        'books':books
    }
    return render(req, 'book-list.html', context)

def BookForm(req):
    if req.method == "POST":
        form = forms.BookForm(req.POST)
        if form.is_valid():
            models.Book.objects.create(
            name = form.cleaned_data['name'],
            price = form.cleaned_data['price'],
            author = form.cleaned_data['author']
            )
            messages.success(req, "Form added")
            return redirect('books')
    else:
        form = forms.BookForm()
    return render(req, 'form_book.html', {'form':form})

def BookDelete(req, id):
    book = get_object_or_404(models.Book, id=id)
    if req.method == "POST":
        book.delete()
        return redirect('books')
    return render(req, 'book_delete.html',  {'book':book})

def BookUpdate(req, id):
    book = get_object_or_404(models.Book, id = id)
    if req.method == "POST":
        form = forms.BookForm(req.POST )
        if form.is_valid():
            form.save()
        return redirect('books')
    else:
        form = forms.BookForm()
    return render(req, 'book_update.html', {'form':form })


def logo(req):
    return render(req, 'logo.html')


# Create your views here.
