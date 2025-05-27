from django.db import models

class Post(models.Model): #dziedziczy po models.Model, co oznacza że jest modelem Django - reprezentuje tabele w BD
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
