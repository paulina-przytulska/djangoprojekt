from django.contrib import admin
from .models import Movie, Showtime, Reservation

admin.site.register(Movie)
admin.site.register(Showtime)
admin.site.register(Reservation)