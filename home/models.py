from django.db import models

# Create your models here.
from django.db import models

class Restaurant(models.Model):
  '''
  Represent a Restaurant Details
  '''
  # Restaurant Name
  name         =  models.CharField(max_length=255,verbose_name='Restaurant name')

  # Restaurant owner name
  owner_name   =  models.CharField(max_length = 255,verbose_name='Restaurant owner name')

  # Restaurant Email

  email        =  models.EmailField(unique = True,verbose_name='email Address')

  # Phone_number 

  phone_number =  models.CharField(max_length=20,null=True,blank=True)
  
  # Address
  address      =  models.CharField(max_length=255,verbose_name='Address')

  # City
  city         =  models.CharField(max_length=255,verbose_name='City')

  # Time Stamp Restauraant 
  created_at   =  models.DateTimeField(auto_now_add = True,verbose_name='TimeStamp')


  def __str__(self):
    return f'{self.name}({self.city})'



