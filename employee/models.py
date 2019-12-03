from django.db import models
from datetime import datetime



class Employee(models.Model):
    employee_name=models.CharField(max_length=50)
    living=models.CharField(max_length=50)
    Hire_date=models.DateTimeField(default=datetime.now,blank=True)
    employee_photo=models.ImageField(upload_to='photos/%Y/%m/%d')
    employee_message=models.CharField(max_length=100 ,blank=True)


    def __str__(self):
         return self.employee_name


