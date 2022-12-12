from django.db import models

# Create your models here.

# Create your models here.
class Files(models.Model):
    #BANKNIFTY,DATE,TIME,OPEN,HIGH,LOW,CLOSE,VOLUME
    banknifty = models.CharField(max_length=150)
    date= models.CharField(max_length=30)
    time=models.TimeField()
    open = models.FloatField()
    high=models.FloatField()
    low=models.FloatField()
    close=models.FloatField()
    volume=models.CharField(max_length=20)
    
    def __str__(self):
        return self.banknifty