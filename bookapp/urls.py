from django.urls import path
from bookapp import views

urlpatterns=[
    path("signup",views.SignupView.as_view(),name="register"),
    path("login",views.LoginView.as_view(),name="signin"),
    path("home",views.IndexView.as_view(),name="index"),
    path("signout",views.SignOutView.as_view(),name="signout"),
    path("books/add",views.BookAddView.as_view(),name="add-book"),
    path("books/all",views.BookListView.as_view(),name="books-list"),
    path("books/remove/<int:id>",views.delete_book,name="remove-book"),
    path("books/details/<int:id>",views.BookDetailsView.as_view(),name="book-detail"),
    path("books/change/<int:id>",views.BookEditView.as_view(),name="edit-book"),
]