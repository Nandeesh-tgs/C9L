from django.db import models
from datetime import datetime
from django.contrib.auth.models import User



class Contact(models.Model):
    product = models.CharField(max_length=200)
    product_id = models.IntegerField()
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    message = models.TextField(blank=True)
    contact_date = models.CharField(max_length=200)
    user_id = models.IntegerField(blank=True)
    def __str__(self):
       return self.name



