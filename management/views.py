from django.shortcuts import render,get_object_or_404, redirect
from .models import Movie, Showtime, Reservation
from django.utils.timezone import now
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

def home(request):
    # Pobieranie parametrów filtrowania z zapytania GET
    search_title = request.GET.get('title', '').strip()  # Usuń białe znaki
    search_date = request.GET.get('date', '').strip()

    # Filtrowanie filmów i seansów
    movies = Movie.objects.all()
    showtimes = Showtime.objects.filter(start_time__gte=now())  # Pokazuj tylko przyszłe seanse

    if search_title:
        movies = movies.filter(title__icontains=search_title)  # Filtruj filmy po tytule
        showtimes = showtimes.filter(movie__title__icontains=search_title)

    if search_date:
        showtimes = showtimes.filter(start_time__date=search_date)  # Filtruj po dacie

    return render(request, 'management/home.html', {
        'movies': movies,
        'showtimes': showtimes,
    })


@login_required
def showtime_details(request, showtime_id):
    showtime = get_object_or_404(Showtime, id=showtime_id)

    if request.method == "POST":
        if showtime.available_seats > 0:
            showtime.available_seats -= 1
            showtime.save()
            messages.success(request, "Rezerwacja zakończona sukcesem!")
        else:
            messages.error(request, "Brak dostępnych miejsc na ten seans.")
        return redirect('home')

    return render(request, 'management/showtime_details.html', {
        'showtime': showtime,
    })


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Po rejestracji przekierowanie na stronę logowania
    else:
        form = UserCreationForm()
    return render(request, 'management/register.html', {'form': form})


@login_required
def my_reservations(request):
    reservations = Reservation.objects.filter(user=request.user)
    return render(request, 'management/my_reservations.html', {'reservations': reservations})