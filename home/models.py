from django.db import models
from django.utils import timezone

class User(models.Model):
    name = models.CharField(max_length=30)
    timein = models.TimeField(null=True)
    timeout = models.TimeField(null=True)
    date = models.DateField(default=timezone.now)



    def __str__(self):
        return self.name
    
class Attendance(models.Model):
    nam = models.CharField(max_length=30)
    phon = models.CharField(max_length=12)
    emaill = models.CharField(max_length=20)
    image = models.CharField(max_length=1000)

    def __str__(self):
        return self.nam
       

class Absentie(models.Model):
    namee = models.CharField(max_length=30)
    dat= models.DateField(null=True)  

    def __str__(self):
        return self.namee
