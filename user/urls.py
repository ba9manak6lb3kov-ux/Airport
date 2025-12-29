from django.urls import path
from . import views



urlpatterns = [
    # Управления (обычного пользователя)
    path('profile_view/', views.profile_view, name='profile'),
    path('airplan_view/', views.airplan_view, name='airplan'),
    path('flights_view/', views.flights_view, name='flights'),
    path('city_list/', views.city_list, name='city_list'),
    path("flights_map/", views.flights_map, name="flights_map"),

    # Управление рейсами (админ)
    path("user/flights/manage/", views.flight_manage, name="flights_manage"),
    path("user/flights/create/", views.flight_create, name="flight_create"),
    path("user/flights/<int:pk>/edit/", views.flight_update, name="flight_update"),



    path("my-bookings/", views.my_bookings, name="my_bookings"),
    path("dashboard/bookings/", views.all_bookings, name="all_bookings"),



    # Управление городами - где есть аэропорты (админ)
    path("user/city/create/", views.city_create, name="city_create"),
    path("user/city/<int:pk>/edit/", views.city_update, name="city_update"),
    path("user/city/<int:pk>/delete/", views.city_delete, name="city_delete"),
    path("user/flights/<int:pk>/delete/", views.flight_delete, name="flight_delete"),

]

