from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home' ),
    path('search/', views.search, name='search' ),
    path("flights/<int:pk>/book/", views.book_flight, name="book_flight"),

]