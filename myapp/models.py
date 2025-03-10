from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    pass 

# Clase para Ingresardatos
class Consume(models.Model):
    month = models.PositiveSmallIntegerField()
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.company}- Month {self.month} - ${self.total_cost}"