from django.db import models

# Create your models here.

class Booking(models.Model):
    name = models.CharField(max_length = 256)
    No_of_guests = models.IntegerField(default = 0)
    BookingDate = models.DateField()
    

class Menu(models.Model):
    Title = models.CharField(max_length = 256)
    Price = models.DecimalField(max_digits=6, decimal_places=2)
    Inventory = models.SmallIntegerField(default=0)
    
    def get_item(self):
        return f'{self.Title} : {str(self.Price)}' 