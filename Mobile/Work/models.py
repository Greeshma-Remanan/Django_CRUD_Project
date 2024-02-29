from django.db import models

# Create your models here.

class Mobile(models.Model):
    brand=models.CharField(max_length=30)
    model=models.CharField(max_length=30)
    price=models.CharField(max_length=20)
    year=models.CharField(max_length=30)
    color=models.CharField(max_length=30)
    image=models.ImageField(upload_to='images',null=True)
