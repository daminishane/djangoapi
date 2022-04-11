from .models import *
from rest_framework import serializers

class BKSerializer(serializers.ModelSerializer):

    class Meta:
        db_table = 'books'
        model = Books
        abstract = True
        fields = '__all__'

class UPSerializer(serializers.ModelSerializer):

    class Meta:
        db_table = 'books'
        model = Books
        abstract = True
        fields = ['book_name','type_book','price']

class URSerializer(serializers.ModelSerializer):

    class Meta:
        db_table = 'users'
        model = users
        abstract = True
        fields = '__all__'

class  ORSerializer(serializers.ModelSerializer):

    class Meta:
        db_table = 'orders'
        model = orders
        abstract = True
        fields = '__all__'
