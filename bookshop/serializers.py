from rest_framework import serializers
from .models import Books, Review
from .models import Contributor
from . import models
class BooksSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Books
        fields = ['id', 'title', 'publisher', 'isbn']


class ContributorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contributor
        fields = ['first_name', 'last_name', 'email']

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review 
        fields = ['content', 'date_created', 'book']

