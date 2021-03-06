from django.db import models


class Hotels(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200, null= False)
    price = models.FloatField()
    available = models.CharField(max_length=10)

    def __str__(self):
        return '%s %s' % (self.name, self.available)


class Bookings(models.Model):
    booking_id = models.BigAutoField(primary_key=True)
    hotel_name = models.CharField(max_length=200, null= False)
    check_in_date = models.DateField(null=False)
    check_out_date = models.DateField(null=False)
    num_of_rooms = models.IntegerField(null=False)
    num_of_guests = models.IntegerField(null=False)
    guest_name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return '%s %s %s' % (self.hotel_name, self.booking_id,self.guest_name)
