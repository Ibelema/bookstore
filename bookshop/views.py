from rest_framework import status
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Books, Review
from .serializers import BooksSerializer, ReviewSerializer
# Create your views here.

@api_view(['GET'])
def list_(request):
    books = Books.objects.all()
    book_serializer = BooksSerializer(books, many=True)
    response = {'message' : 'this is the list of books on the counter --> ', 'book':book_serializer.data}
    return Response(response, status=status.HTTP_200_OK)


@api_view(['GET'])
def book_detail(request, pk):
    try:
        book = Books.objects.get(pk=pk)
    except Books.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
#retrieve

    if request.method == 'GET':
        serializer = BookskSerializer(book, data)
        return Response(serializer.data, status=status.HTTP_200_OK)
#update
@api_view(['PUT'])
def update_book(request, pk): 
    if request.method =='PUT':
        book = Books.objects.get(pk=pk)
        data=request.data
        serializer = BooksSerializer(book, data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'this book is about to be updated'}, serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#delete
@api_view(['DELETE'])
def delete_book(request, pk):
    if request.method == 'DELETE':
        book = Books.objects.get(pk=pk)
        book.delete()
        return Response({'message':'this book has been deleted'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['PUT'])
def update_review(request, id):
    if request.method == 'PUT':
        review = Review.objects.get(id=id)
        data = request.data
        review_serializer = ReviewSerializer(review, data)
        if review_serializer.is_valid():
            review_serializer.save()
            return Response({'instruction':'you are given the opportunity to update your comment'}, review_serializer.data)
        return Response(review_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_review(request, pk):
    if request.method == 'DELETE':
        review = Review.objects.get(pk=pk)
        review.delete()
        return Response({'message':'this review has been deleted'}, status=status.HTTP_204_NO_CONTENT)