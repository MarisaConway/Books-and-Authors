from django.db import models


class books(models.Model):
    title = models.CharField(max_length = 255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)


class authors(models.Model):
    first_name = models.CharField(max_length = 45)
    last_name = models.CharField(max_length = 45)
    books = models.ManyToManyField(books, related_name = "books_authors")
    notes = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)



# do I need to add on_delete = models.CASCADE 
# FOR my books foriegn key









# Create your models here.
