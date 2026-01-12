from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(verbose_name="Описание", blank=True)
    image = models.ImageField(upload_to='restaurants/', blank=True, null=True)
    opening_hours = models.CharField(max_length=50, verbose_name="Часы работы", blank=True)

    def __str__(self):
        return self.name
