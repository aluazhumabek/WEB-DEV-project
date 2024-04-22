from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()

class Genre(models.Model):
    id = models.AutoField(primary_key=True,editable=True)
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=255)
    genres = models.ManyToManyField(Genre, related_name='movies')
    description = models.TextField()
    release_date = models.DateField()
    rating = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.title

class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")
    text = models.TextField() # Review itself
    rating = models.IntegerField()
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.username} on {self.movie.title}"

