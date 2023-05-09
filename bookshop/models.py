from django.db import models
from django.contrib import auth

# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length=50, help_text='the name of the publisher')
    website = models.URLField(help_text="the publisher's website.")
    email = models.EmailField(help_text='the publisher')

    def __str__(self):
        return self.name


class Books(models.Model):
    title = models.CharField(max_length=30)
    genre = models.CharField(max_length=15)
    isbn = models.CharField(max_length=13, verbose_name='ISBN number of the book')
    content = models.TextField()
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Contributor(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.first_name
    

class Review(models.Model):
    content = models.TextField()
    rating = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(auth.get_user_model(), on_delete=models.CASCADE)
    book = models.ForeignKey(Books, on_delete=models.CASCADE, help_text='tbe book that this review is for..')