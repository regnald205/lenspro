from django.db import models
from datetime import datetime



class Activity(models.Model):
   
    title=models.CharField(max_length=100)
    venue_name=models.CharField(max_length=50)
    place=models.CharField(max_length=50)
    price=models.IntegerField()
    ##CAMERA_USED_CHOICES=[
    ###    ('nikon700','Nikon700'),
     ##   ('nikon800','Nikon800'),
      ## ]
    camera_used=models.CharField(max_length=20)
    Event_date=models.DateTimeField(default=datetime.now,blank=True)
    videoField=models.FileField(upload_to='videos/%Y/%m/%d/',blank=True)
    is_finished_pay=models.BooleanField(default=True)


    def __str__(self):
         return self.title
    


