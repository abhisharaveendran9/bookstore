from django import forms
from django.contrib.auth.models import User
from bookapp.models import Books

# class RegistrationForm(forms.Form):
#     first_name=forms.CharField()
#     last_name=forms.CharField()
#     email=forms.EmailField()
#     username=forms.CharField()
#     password=forms.CharField()

class RegistrationForm(forms.ModelForm):
    class Meta:
        model=User
        fields=["first_name","last_name","username","email","password"]
        widgets = {

            "password": forms.PasswordInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "username": forms.TextInput(attrs={"class": "form-control"}),
        }

class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))

class BookForm(forms.ModelForm):  #add view
    class Meta:
        model=Books
        fields=["book_name","author_name","price","quantity","publisher"]

        widgets={
            "book_name":forms.TextInput(attrs={"class":"form-control"}),
            "author_name":forms.TextInput(attrs={"class":"form-control"}),
            "price":forms.NumberInput(attrs={"class":"form-control"}),
            "quantity":forms.NumberInput(attrs={"class":"form-control"}),
            "publisher":forms.TextInput(attrs={"class":"form-control"}),

        }

class BookChangeForm(forms.ModelForm):
    class Meta:
        model=Books
        fields=("__all__")
