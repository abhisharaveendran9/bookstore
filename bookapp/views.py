from django.shortcuts import render,redirect
from django.views.generic import View
from bookapp import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from bookapp.models import Books
from django.contrib import messages


# Create your views here.

class SignupView(View):

    def get(self,request,*args,**kwargs):
        form=forms.RegistrationForm()
        return render(request,"registration.html",{"form":form})

    def post(self,request,*args,**kwargs):
        form=forms.RegistrationForm(request.POST)
        if form.is_valid():
            User.objects.create_user(**form.cleaned_data)
            messages.success(request, "your account has been created")
            return redirect("signin")

        else:
            messages.error(request, "registration failed")
            return render(request,"registration.html",{"form":form})


class LoginView(View):
    def get(self,request,*args,**kwargs):
        form=forms.LoginForm()
        return render(request,"login.html",{"form":form})

    def post(self,request,*args,**kwargs):
        # print(request.POST.get("username"))
        # print(request.POST.get("password"))
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            uname = form.cleaned_data.get("username")
            pwd = form.cleaned_data.get("password")
            user = authenticate(request, username=uname, password=pwd)
            if user:
                login(request, user)
                messages.success(request, "successfully login")
                print("login success")
                return redirect("index")
            else:
                messages.error(request, "invalid username or password")
                print("invalid credentials")
                return render(request, "login.html",{"form": form})

        return render(request,"login.html")


class IndexView(View):

    def get(self,request,*args,**kwargs):
        return render(request,"home.html")


class SignOutView(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("signin")


class BookAddView(View):

    def get(self,request,*args,**kwargs):
        form=forms.BookForm()
        return render(request,"add-book.html",{"form": form})

    def post(self,request,*args,**kwargs):
        form=forms.BookForm(request.POST)
        if form.is_valid():
            form.instance.user=request.user
            form.save()
            messages.success(request, "book has been added")
            return redirect("index")
        else:
            messages.error(request, "failed")
            return render(request,"add-book.html",{"form": form})


class BookListView(View):

    def get(self,request,*args,**kwargs):
        all_books=Books.objects.all()
        return render(request,"booklist.html",{"books":all_books})


#localhost:8000/books/remove/id
def delete_book(request,*args,**kwargs):
    id=kwargs.get("id")
    Books.objects.get(id=id).delete()
    messages.success(request, "deleted")
    return redirect("books-list")


class BookDetailsView(View):

    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        book=Books.objects.get(id=id)
        return render(request,"book-detail.html",{"book":book})


class BookEditView(View):

    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        book=Books.objects.get(id=id)
        form=forms.BookChangeForm(instance=book)
        return render(request,"book-edit.html",{"form":form})

    def post(self,request,*args,**kwargs):
        id=kwargs.get("id")
        book=Books.objects.get(id=id)
        form=forms.BookChangeForm(request.POST,instance=book)

        if form.is_valid():
            form.save()
            # messages.success(request,"book hasbeen changed")
            return redirect("books-list")
        else:
            # messages.error(request,"book update failed")
            return render(request,"book-edit.html",{"form":form})

