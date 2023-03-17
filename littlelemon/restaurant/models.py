from django.db import models

# Create your models here.
class Bookingtable(models.Model):
    name = models.CharField(max_length=255) 
    no_of_guests = models.IntegerField() 
    BookingDate = models.DateTimeField() 
    
    
    
class Menutable(models.Model):
    title = models.CharField(max_length=255) 
    price = models.DecimalField(max_digits=6,decimal_places=2) 
    inventory = models.SmallIntegerField() 
    
    
    