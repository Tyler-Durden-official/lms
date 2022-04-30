from django import forms
from django.contrib.auth.models import User
from matplotlib.style import available
from .models import Book, Student

class IssueBookForm(forms.Form):
    books = Book.objects.filter(availability__gt = 0)
    book_id2 = forms.ModelChoiceField(queryset=books, empty_label="Book Name [book_id]", to_field_name="book_id", label="Book (Name and book_id)")
    name2 = forms.ModelChoiceField(queryset=Student.objects.all(), empty_label="Name [Branch] [Roll No]", to_field_name="user", label="Student Details")
    book_id2.widget.attrs.update({'class': 'form-control'})
    name2.widget.attrs.update({'class':'form-control'})
