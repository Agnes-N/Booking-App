from django.db import models
# Create your models here.

class Apartment(models.Model):
    ROOMS = (
        ('Private', 'Private'),
        ('Public', 'Public'),
        ('Executive', 'Executive'),
        ('Suite', 'Suite'),
        ('Presidential', 'Presidential'),
    )
    rooms = models.CharField(choices=ROOMS, max_length = 255, null = True)

    number_of_guests = models.IntegerField(default = 0, null = True)
    location = models.CharField(max_length = 255, null = True)

    def __str_(self):
        return "Apartment for {}".format(self.rooms)