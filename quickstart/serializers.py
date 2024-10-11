from rest_framework import serializers
from .models import Location
from .models import User
from .models import Discount
from .models import Furniture
from .models import Ticket
from .models import Ticketimage



class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = '__all__'


class FurnitureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Furniture
        fields = '__all__'
        read_only_fields = ['furnitureId']  # Exclude this field from being required on POST

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'

class TicketImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticketimage
        fields = '__all__'


