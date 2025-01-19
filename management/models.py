from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.PositiveIntegerField()  # To będzie w minutach

    def __str__(self):
        return self.title

class Showtime(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    available_seats = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.movie.title} - {self.start_time}"

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    showtime = models.ForeignKey(Showtime, on_delete=models.CASCADE)
    reserved_at = models.DateTimeField(auto_now_add=True)
