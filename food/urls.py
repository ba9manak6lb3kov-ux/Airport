from django.urls import path
from . import views

urlpatterns = [
    path('foodcourt/', views.food_view, name='food'),
]
