from django.urls import path
from .views import list_, book_detail, update_book, delete_book, update_review, delete_review
urlpatterns = [
    #path('', book_counter),
    path('list/', list_ ),
    path('single/<int:pk>/', book_detail),
    path('update/<int:pk>/', update_book),
    path('delete/<int:pk>/', delete_book),
    path('updatereview/<int:id>/', update_review),
    path('deletereview/<int:pk>/', delete_review),
]