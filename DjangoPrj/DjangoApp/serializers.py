from rest_framework import serializers
from .models import Hotels, Bookings


class HotelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Hotels
        fields = ["name", "price", "available"]


class BookingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Bookings
        fields = ["hotel_name", "check_in_date", "check_out_date"]
