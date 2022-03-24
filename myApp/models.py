from django.db import models
from django_countries.fields import CountryField

class Location(models.Model):
    country = CountryField(blank_label='(select country)', blank=True)
    street_address = models.CharField(max_length = 255, null = True)
    Access_code = models.CharField(max_length = 255, null = True, blank=True)

    def __str_(self):
        return "Apartment for {}".format(self.country)

class Amnesities(models.Model):
    AMNESITIES = (
        ('Essentials', 'Essentials'),
        ('Wifi', 'Wifi'),
        ('TV', 'TV'),
        ('Heat', 'Heat')
    )
    amneties = models.CharField(choices=AMNESITIES, max_length = 255, null = True)

    def __str_(self):
        return "Apartment for {}".format(self.amneties)

class GuestsRoom(models.Model):
    BEDROOMS = (
        ('Studio', 'Studio'),
        ('Ordinary', 'Ordinary'),
        ('Officetel', 'Officetel'),
        ('Penthouse', 'Penthouse')
    )
    bedrooms = models.CharField(choices=BEDROOMS, max_length = 255, null = True)

    guests = models.IntegerField(default = 0, null = True)
    beds = models.IntegerField(default = 0, null = True)

    def __str_(self):
        return "Apartment for {}".format(self.bedrooms)

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

    apart_location = models.ForeignKey(Location, related_name='apartment_location', on_delete=models.CASCADE, null = True)
    amnesity = models.ForeignKey(Amnesities, related_name='apartment_amnesity', on_delete=models.CASCADE, null = True)
    guestroom = models.ForeignKey(GuestsRoom, related_name='apartment_guestsroom', on_delete=models.CASCADE, null = True)

    def __str_(self):
        return "Apartment for {}".format(self.rooms)