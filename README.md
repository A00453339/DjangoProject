# DjangoProject
This repo maintains the code packet for hotel reservation rest api implemented using Django rest framework

This RestAPi implements a basic varsion of hotel reservation system. It uses Django rest framework for this purpose.

The backend of this application consists of following 2 tables:-
Hotels
id = Auto generated primary_key
name = Hotel name, null= False
price = Hotel room price
available = (YES or NO). Whether hotel room is avaailable or not.

Bookings
booking_id = Auto generated primary key
hotel_name = Hotel name
check_in_date = date for check-in
check_out_date = date for check-out
num_of_rooms = number of rooms requested
num_of_guests = number of guests expected
guest_name = Name of one of the guests

Following are the urls for 2 GET requests supported by the application:-
1) http://127.0.0.1:8000/app/hotel_list/ - This will display all the hotels present in Hotels table
2) http://127.0.0.1:8000/app/bookings/ - This will display all the bookings made so far.
3) http://127.0.0.1:8000/app/bookings/<booking_id> - This will display the booking details for the booking id passed in GET request.
4) http://127.0.0.1:8000/app/bookings/Gagan/<guest_name> - This will display all the bookings made by a guest.

Following are the urls for 2 POST requests supported by the application:-
1) http://127.0.0.1:8000/app/hotel_list/ - Sample request

{
	"name" : "TAJ",
	"price" : 270.00,
	"available" : "NO"
}

2) http://127.0.0.1:8000/app/booking/ - Sample requests

{
	"hotel_name":"TAJ",
	"check_in_date":"2022-04-01",
	"check_out_date":"2022-04-03",
	"num_of_rooms":2,
	"num_of_guests":4,
	"guest_name":"Gagan"
}

Also, following validations are built-in in order to introduce complexity
1) Check-in date cannot be blank
2) Check-out date cannot be blank
3) Check-out date cannot be earlier than check-in date
4) Hotel shold be present in Hotels table in order to make bookings
5) Hotel shold be marked as available in Hotels table in order to make bookings
6) Maximum of 2 guests are allowed in a room. Therefore, number of guests should not be greater than number of rooms*2
