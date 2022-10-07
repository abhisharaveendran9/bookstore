from rest_framework.serializers import ModelSerializer
from bookapp.models import Books
from rest_framework import serializers

class BookSerializer(ModelSerializer):
    # user=serializers.CharField(read_only=True)

    class Meta:
        model=Books
        fields="__all__"

    def create(self, validated_data):
        # user=self.context.get("user")
        book_name=self.context.get("book_name")
        return Books.objects.create(**validated_data,book_name=book_name)