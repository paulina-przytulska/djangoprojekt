from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),  # Strona główna
    path('login/', auth_views.LoginView.as_view(template_name='management/login.html'), name='login'), # Logowanie
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Wylogowanie
    path('register/', views.register, name='register'),  # Rejestracja użytkownika
    path('showtime/<int:showtime_id>/', views.showtime_details, name='showtime_details'),  # Szczegóły seansu
]

