from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile_view, name='profile'),
    path('airplan_view/', views.airplan_view, name='airplan'),
    path('flights_view/', views.flights_view, name='flights'),
    path('City/', views.City, name='City'),
    # path('City_list/', views.City_list, name='City_list'),
]

