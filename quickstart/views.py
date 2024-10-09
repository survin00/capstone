
from rest_framework import viewsets
from .models import Location
from .models import User
from .models import Discount
from .models import Furniture
from .models import Ticket
from .models import Ticketimage

from .serializers import LocationSerializer
from .serializers import UserSerializer
from .serializers import DiscountSerializer
from .serializers import FurnitureSerializer
from .serializers import TicketSerializer
from .serializers import TicketImageSerializer

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class DiscountViewSet(viewsets.ModelViewSet):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer

class FurnitureViewSet(viewsets.ModelViewSet):
    queryset = Furniture.objects.all()
    serializer_class = FurnitureSerializer

class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


class TicketImageViewSet(viewsets.ModelViewSet):
    queryset = Ticketimage.objects.all()
    serializer_class = TicketImageSerializer


