from management.models import Movie, Showtime
from django.utils.timezone import make_aware
from datetime import datetime

def populate_data():
    # Tworzenie filmów
    movie1 = Movie.objects.create(
        title="Kosmiczne Przebudzenie",
        description="Ziemia stoi w obliczu zagłady, gdy nieznane siły z kosmosu zaczynają destabilizować układ słoneczny...",
        duration=130
    )
    movie2 = Movie.objects.create(
        title="CyberPunk: Ostatni Kod",
        description="W świecie, gdzie granica między człowiekiem a maszyną jest coraz bardziej zacierana...",
        duration=142
    )
    movie3 = Movie.objects.create(
        title="Cień Wieczności",
        description="Tajemnicze morderstwo w małym miasteczku prowadzi do odkrycia pradawnej klątwy...",
        duration=120
    )

    # Tworzenie seansów
    Showtime.objects.create(
        movie=movie1,
        start_time=make_aware(datetime(2025, 12, 30, 18, 0)),
        available_seats=50
    )
    Showtime.objects.create(
        movie=movie2,
        start_time=make_aware(datetime(2025, 12, 31, 20, 0)),
        available_seats=75
    )
    Showtime.objects.create(
        movie=movie3,
        start_time=make_aware(datetime(2025, 1, 1, 17, 0)),
        available_seats=60
    )

    print("Dane testowe zostały pomyślnie dodane!")
