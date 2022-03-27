from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ApartmentViewSet, LocationViewSet, AmnesitiesViewSet, GuestsRoomViewSet

router = DefaultRouter()
router.register(r'apartment', ApartmentViewSet)
router.register(r'location', LocationViewSet)
router.register(r'amnesity', AmnesitiesViewSet)
router.register(r'guest', GuestsRoomViewSet)

urlpatterns = [
    path("", include(router.urls))
]
