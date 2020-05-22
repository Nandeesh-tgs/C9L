from django.db import models
from datetime import datetime
from suppliers.models import Supplier

class Products(models.Model):
    supplier=models.ForeignKey(Supplier,on_delete=models.DO_NOTHING)
    title=models.CharField(max_length=200)
    description=models.TextField(blank=True)
    Num_Stops=models.IntegerField()
    Machine_room=models.CharField(max_length=200)
    Passenger=models.IntegerField()
    door_size=models.IntegerField()
    shaft_width=models.IntegerField()
    shaft_depth=models.IntegerField()
    shaft_pit=models.IntegerField()
    shaft_overhead=models.IntegerField()
    Price=models.IntegerField()
    photo_main=models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1=models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2=models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3=models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4=models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5=models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_6=models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published= models.BooleanField(default=True)
    product_date=models.DateField(default=datetime.now, blank=True)
    def __str__(self):
        return self.title
    

    
    







