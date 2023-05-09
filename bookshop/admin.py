from django.contrib import admin
from .models import Books, Contributor, Review, Publisher
# Register your models here.
admin.site.register(Books)
admin.site.register(Publisher)
admin.site.register(Contributor)
admin.site.register(Review)