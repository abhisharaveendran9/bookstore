from django.shortcuts import render

# Create your views here.

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from api.serializers import BookSerializer
from bookapp.models import Books
from rest_framework import authentication,permissions
from django.contrib.auth.models import User


class BooksView(ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    # def get_queryset(self):
    #     return Books.objects.filter(user=self.request.user)
    #
    # def create(self, request, *args, **kwargs):
    #     serializer=BookSerializer(data=request.data,context={"user":request.user})
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(data=serializer.data)
    #     else:
    #         return Response(data=serializer.errors)