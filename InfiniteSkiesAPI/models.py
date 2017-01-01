from django.db import models

# Create your models here.

class data(models.Model):
    date = models.DateField( blank=True)
    title = models.CharField(max_length=100)
    copyright=models.CharField(max_length=100)
    hdurl=models.CharField(max_length=1500)
    url=models.CharField(max_length=1500)
    media_type=models.CharField(max_length=15)
    service_ver=models.CharField(max_length=15)
    explanation = models.TextField(max_length=7000)

    def __str__(self):
        return self.title+' (date: '+str(self.date)+')'



