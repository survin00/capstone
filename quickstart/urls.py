from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LocationViewSet
from .views import UserViewSet
from .views import DiscountViewSet
from .views import FurnitureViewSet
from .views import TicketViewSet
from .views import TicketImageViewSet

router = DefaultRouter()
router.register(r'location',LocationViewSet)
router.register(r'user',UserViewSet)
router.register(r'discounts', DiscountViewSet)
router.register(r'furniture', FurnitureViewSet)
router.register(r'ticket', TicketViewSet)
router.register(r'ticketimage', TicketImageViewSet)

urlpatterns = [
    path('',include(router.urls)),
]   