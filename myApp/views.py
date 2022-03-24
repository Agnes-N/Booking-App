# from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ApartmentSerializer, LocationSerializer, AmnesitiesSerializer, GuestsRoomSerializer
from .models import Apartment, Location, Amnesities, GuestsRoom

class ApartmentViewSet(viewsets.ModelViewSet):
    serializer_class = ApartmentSerializer
    queryset = Apartment.objects.all()

class LocationViewSet(viewsets.ModelViewSet):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()

class AmnesitiesViewSet(viewsets.ModelViewSet):
    serializer_class = AmnesitiesSerializer
    queryset = Amnesities.objects.all()

class GuestsRoomViewSet(viewsets.ModelViewSet):
    serializer_class = GuestsRoomSerializer
    queryset = GuestsRoom.objects.all()
