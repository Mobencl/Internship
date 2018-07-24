from django.db import models
from SportcenterApp.models import Terrain, Sportcenters
# Create your models here.
from django.contrib.auth.models import User
from SportcenterProject import settings
from SportcenterApp.models import Terrain
import uuid
# class bookingStatus():



class Booking(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    sportcenter = models.ForeignKey(Sportcenters, on_delete = models.CASCADE)
    terrain = models.ForeignKey(Terrain, on_delete = models.CASCADE)
    Address = models.CharField(max_length = 255)
    email = models.EmailField(max_length=254)
    check_in = models.DateTimeField(blank =True,null=True)
    check_out = models.DateTimeField(blank=True,null=True)
    creation_date= models.DateTimeField(auto_now_add=True)
    booking_id = models.CharField(max_length=254,default=uuid.uuid4())
    #booking_status = models.ForeignKey()// I have to create an other class fot the booking status
    #time_period = models.PositiveIntegerField(blank=True, null=True)
    day_period = models.PositiveIntegerField(blank=True,null=True)
    capacity = models.PositiveIntegerField(blank=True,null=True)
    #bookingStatus is really important ! I have to add a class for bookingStatus
    #time_unit = models.CharField(default = getattr(settings,'BOOKING_TIME_INTERVAL'))
    #date = models.DateTimeField(blank=True)
# FOR GUESTS WHO WANTS TO JOIN THE GAME
#class Guest(models.Model):
#    guest = models.ForeignKey(User,on_delete=models.CASCADE)

class terrainAvailibility(models.Model):
    terrain = models.ForeignKey(Terrain,on_delete=models.CASCADE)
    sportcenter = models.ForeignKey(Sportcenters,on_delete=models.CASCADE)
    notAvailableFrom = models.DateTimeField(blank =True, null=True)
    notAvailableTill = models.DateTimeField(blank=True, null=True)









#class BookingTerrain(models.Model):
#    persons = models.PositiveIntegerField()
#    terrain_id= models.PositiveIntegerFiel()
#    booking = models.ForeignKey(Booking,on_delete = models.ON_CASCADE)
