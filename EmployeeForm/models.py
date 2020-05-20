from django.db import models
from datetime import date

# Create your models here.
class Employee_Model(models.Model):
    name = models.CharField(max_length = 26, default='empty')
    address = models.CharField(max_length = 50, default='empty')
    city = models.CharField(max_length = 16, default='empty')
    state = models.CharField(max_length = 16, default='empty')
    zip_code = models.IntegerField(default='92')
    email = models.EmailField(max_length = 17,default='myfuck@gmail.com')
    password = models.CharField(max_length = 50, default='flkjsaf')
    social_security = models.CharField(max_length = 26, default='empty')
    hire_date = models.DateField(default=date.today)
    birth_date = models.DateField(default=date.today)
    hourly_rate = models.FloatField(min_value=0, max_value=100, default=10)
    title = models.CharField(max_length = 26, default='empty')
    status = models.CharField(max_length = 26, default='empty')
    gender = models.CharField(max_length = 7, default='male')
    worked_before = models.BooleanField(default=True)


