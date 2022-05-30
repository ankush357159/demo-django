from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.first_name



class Album(models.Model):
    title = models.CharField(max_length=30)
    artist = models.CharField(max_length=30)
    genre = models.CharField(max_length=30)

    def __str__(self):
        return self.title

class Song(models.Model):
    name = models.CharField(max_length=100)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=30)
    genre = models.CharField(max_length=30)
    writer = models.CharField(max_length=30)

    def __str__(self):
        return self.author

class Author(models.Model):
    name = models.ForeignKey(Book, on_delete=models.CASCADE)
    dob = models.DateField()

    def __str__(self):
        return self.name




class Snippet(models.Model):
    created = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)

    