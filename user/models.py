from django.contrib.auth.models import User
from django.db import models


class City(models.Model):
    name = models.CharField("Город", max_length=100)
    region = models.CharField("Область", max_length=100)
    latitude = models.FloatField("Широта")
    longitude = models.FloatField("Долгота")

    def __str__(self):
        return f"{self.name} ({self.region})"


class Flight(models.Model):
    airline = models.CharField("Авиакомпания", max_length=100)
    origin = models.ForeignKey(
        City,
        related_name="departures",
        on_delete=models.CASCADE,
        verbose_name="Город вылета"
    )
    destination = models.ForeignKey(
        City,
        related_name="arrivals",
        on_delete=models.CASCADE,
        verbose_name="Город прилёта"
    )
    departure_time = models.DateTimeField("Время вылета")
    arrival_time = models.DateTimeField("Время прилёта")
    status = models.CharField("Статус", max_length=50)
    seats_available = models.IntegerField("Свободные места", default=100)
    class_type = models.CharField(
        "Класс",
        max_length=20,
        choices=[("Эконом", "Эконом"), ("Бизнес", "Бизнес")],
        default="Эконом"
    )

    def __str__(self):
        return f"{self.airline}: {self.origin} → {self.destination}"

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    tickets = models.PositiveIntegerField()
    booked_at = models.DateTimeField(auto_now_add=True)
