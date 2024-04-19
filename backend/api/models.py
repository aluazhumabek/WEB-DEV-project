from django.db import models
from django.conf import settings
from django.contrib.auth.models import User # built-in class User

class Movie(models.Model):
    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    description = models.TextField()
    release_date = models.DateField()
    rating = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.title

class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="reviews")
    text = models.TextField() # Review itself
    rating = models.IntegerField()
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.username} on {self.movie.title}"

class MovieList(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="movie_lists")
    name = models.CharField(max_length=255) # name is given by user, like {"Favorites", "Watching rn", ... etc}
    movies = models.ManyToManyField(Movie, related_name="lists")
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} by {self.user.username}"
