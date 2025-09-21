from django import forms
from .models import Author

class AuthorForm(forms.Form):
    name = forms.CharField(max_length=200, label='Author name', widget=forms.TextInput({'class':'name-form', 'placeholder':'Author name'}))
    surname = forms.CharField(max_length=200, label='Author surname', widget=forms.TextInput({'class':'name-form', 'placeholder':'Author surname'}))
    bio = forms.CharField(label='Author bio', widget=forms.TextInput({'class':'name-form', 'placeholder':'Author bio'}))

class BookForm(forms.Form):
    name = forms.CharField(max_length=200, label='Book name', widget=forms.TextInput({'class':'name-form', 'placeholder':'Book name'}))
    price = forms.IntegerField(label='Price', widget=forms.NumberInput({'class':'name-form', 'placeholder':'Price'}))
    author = forms.ChoiceField()
    author = forms.ModelChoiceField(queryset=Author.objects.all(),label='Author',widget=forms.Select(attrs={'class': 'name-form', 'placeholder':'Choice Author'}))







