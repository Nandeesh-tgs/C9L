from django.db import models


class Supplier(models.Model):

   company_name=models.CharField(max_length=200)
   logo=models.ImageField(upload_to='photos/%Y/%m/%d/')
   address=models.CharField(max_length=200)
   city=models.CharField(max_length=200)
   state=models.CharField(max_length=200)
   pincode=models.CharField(max_length=200)
   about_company=models.TextField(blank=True)
   c9lcust_feedback=models.CharField(max_length=200)
   is_mvp=models.BooleanField(default=False)
   def __str__(self):
       return self.company_name

   


   

