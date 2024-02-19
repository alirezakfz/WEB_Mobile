from django.db import models

# Create your models here.

class Booking(models.Model):
   first_name = models.CharField(max_length=200)    
   last_name = models.CharField(max_length=200)
   guest_number = models.IntegerField()
   comment = models.CharField(max_length=1000)

   def __str__(self):
      return self.first_name + ' ' + self.last_name


class Category(models.Model):
   slug = models.SlugField()
   title = models.CharField(max_length = 255)

   def __str__(self):
      return self.title 



# Menu model
class MenuItem(models.Model):
   name = models.CharField(max_length = 200)
   price = models.DecimalField(max_digits=5, decimal_places=2)
   inventory = models.IntegerField(default=0)
   category = models.ForeignKey(Category, on_delete= models.PROTECT, default = 1)
   description = models.CharField(max_length=1000, default='', blank=True)

   def __str__(self):
      return self.name