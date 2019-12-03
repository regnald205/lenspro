from django.db import models
from datetime import datetime


class Upload(models.Model):
     Event_title=models.CharField(max_length=200,blank=True)
     event_photos=models.ImageField(upload_to='photos/%Y/%m/%d',blank=True)
     CEO_photo = models.ImageField(upload_to='photos/%Y/%m/%d',blank=True)
     Event_date=models.DateTimeField(default=datetime.now,blank=True)

     def __str__(self):
         return self.Event_title

 





