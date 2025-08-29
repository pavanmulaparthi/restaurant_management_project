from django.db import models

# Create your models here.
class Restaurant(models.Model):
    phone_number = models.CharField()
    updated_at   = models.DateTimeField(auto_now_add=True)
    name         = models.CharField(max_length=255)

   def __str__(self):
       return self.phone_number
