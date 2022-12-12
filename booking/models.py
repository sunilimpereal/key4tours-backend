from pyexpat import model
from unicodedata import category, name
from django.db import models
from account.models import User

from package.models import Duration, HolidayPackage, PriceCategory

# Create your models here.


class HolidayBooking(models.Model):
    id                = models.AutoField(primary_key=True)
    number            = models.CharField(max_length=255)
    selected_duration = models.ForeignKey(Duration, on_delete=models.CASCADE)
    selected_category = models.ForeignKey(PriceCategory, on_delete=models.CASCADE)
    package_id        = models.ForeignKey(HolidayPackage, on_delete=models.CASCADE)
    uid               = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_id        = models.CharField(max_length=255)
    start_date        = models.DateTimeField()
    end_date          = models.DateTimeField()
    grand_total          = models.DecimalField(decimal_places=2,max_digits=12,null=True)

    def __str__(self):
        return self.number
    
class Room(models.Model):
    id             = models.AutoField(primary_key=True)
    room_no        = models.CharField(max_length=255,default='')
    holidayBooking = models.ForeignKey(HolidayBooking,related_name='rooms',on_delete=models.CASCADE)
    def __str__(self):
        return self.holidayBooking.number + "room : "+self.room_no

class Person(models.Model):
    id          = models.AutoField(primary_key=True)
    gender      = models.CharField(max_length=255)
    first_name  = models.CharField(max_length=255)
    last_name   = models.CharField(max_length=255)
    dob         = models.DateTimeField()
    passport_no = models.CharField(max_length=255)
    room        = models.ForeignKey(Room, related_name='persons',on_delete=models.CASCADE)
    
    def __str__(self):
        return self.first_name
    

