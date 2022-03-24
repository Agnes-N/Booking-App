from django.contrib import admin
from .models import Apartment, Location, Amnesities, GuestsRoom

admin.site.register(Apartment)
admin.site.register(Location)
admin.site.register(Amnesities)
admin.site.register(GuestsRoom)
