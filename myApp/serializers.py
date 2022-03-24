from django_countries.serializers import CountryFieldMixin
from rest_framework import serializers
from .models import Apartment, Location, Amnesities, GuestsRoom

class ApartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apartment
        fields = (
            "id",
            "rooms",
            "number_of_guests",
            "location",
            "apart_location",
            "amnesity",
            "guestroom"
        )

class LocationSerializer(CountryFieldMixin, serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = (
            "id",
            "country",
            "street_address",
            "Access_code"
        )

class AmnesitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Amnesities
        fields = (
            "id",
            "amneties",
        )

class GuestsRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuestsRoom
        fields = (
            "id",
            "bedrooms",
            "guests",
            "beds"
        )
