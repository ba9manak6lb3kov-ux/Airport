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
    origin = models.ForeignKey(City, on_delete=models.CASCADE, related_name="departures", verbose_name="Город вылета")
    destination = models.ForeignKey(City, on_delete=models.CASCADE, related_name="arrivals", verbose_name="Город прилёта")
    departure_time = models.DateTimeField("Время вылета")
    arrival_time = models.DateTimeField("Время прилёта")
    status = models.CharField("Статус", max_length=50, default="Запланирован")

    def __str__(self):
        return f"{self.airline}: {self.origin} → {self.destination}"





