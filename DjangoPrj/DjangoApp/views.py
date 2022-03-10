from django.shortcuts import render
from django.http import HttpResponse
from .models import Hotels, Bookings
from .serializers import HotelSerializers, BookingSerializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from datetime import datetime
import pickle


def home(request):
    return HttpResponse("<h1> Hello Canada </h1>")


@api_view(['GET', 'POST'])
def hotel_details(request):
    if request.method == "GET":
        hotel_list = Hotels.objects.all()
        hotel_get_serializer = HotelSerializers(hotel_list, many=True)
        return Response(hotel_get_serializer.data)
    if request.method == "POST":
        hotel_val = request.data
        hotel_post_serializer = HotelSerializers(data=hotel_val)
        if hotel_post_serializer.is_valid():
            hotel_post_serializer.save()
        return Response({"Message": request.data["name"] + " Added Successfully"})


@api_view(['GET', 'POST'])
def booking_details(request):
    if request.method == "GET":
        book_dtl = Bookings.objects.all()
        book_get_serializer = BookingSerializers(book_dtl, many=True)
        return Response(book_get_serializer.data)
    if request.method == "POST":
        book_val = request.data
        hotel_name = request.data["hotel_name"]
        hotel_check = Hotels.objects.filter(name=hotel_name)
        hotel_avb = Hotels.objects.filter(name=hotel_name).filter(available='YES')
        booking_post_serializer = BookingSerializers(data=book_val)
        new_check_out_date = datetime.strptime(request.data["check_out_date"], '%Y-%m-%d')
        new_check_in_date = datetime.strptime(request.data["check_in_date"], '%Y-%m-%d')
        if not hotel_check.exists():
            return Response({"Please create the hotel before booking"})
        elif not hotel_avb.exists():
            return Response({"All the rooms are currently booked for the requested hotel"})
        elif "check_out_date" not in request.data:
            return Response({"Check out date cannot be blank"})
        elif "check_in_date" not in request.data:
            return Response({"Check in date cannot be blank"})
        elif new_check_out_date < new_check_in_date:
            return Response({"Check out date cannot be earlier than check in date"})
        elif booking_post_serializer.is_valid():
            booking_post_serializer.save()
        return Response({"Message": request.data["hotel_name"] + " Booked Successfully"})


@api_view(['GET'])
def hotel_filters(request, pk):
    if request.method == "GET":
        hotel_list = Hotels.objects.get(id=pk)
        hotel_get_serializer = HotelSerializers(hotel_list, many=False)
        return Response(hotel_get_serializer.data)

