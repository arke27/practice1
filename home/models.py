from django.db import models

# Create your models here.

class Student_Model(models.Model):

    # id = models.AutoField() -- this field is automatically by django
    name = models.CharField(max_length=150)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.TextField()
    image = models.ImageField()
    file = models.FileField()

class Car_Model(models.Model):
    car_name = models.CharField(max_length=500)
    speed = models.IntegerField(default=50)
    

