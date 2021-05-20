from django.db import models

# Create your models here.
class rcrops(models.Model):
    
    rcrop_image=models.ImageField(upload_to = 'pics')
    rcrop_name=models.CharField(max_length = 50)
    rcrop_description=models.TextField()
    rcrop_url=models.CharField(max_length = 50)

class kcrops(models.Model):
    
    kcrop_image=models.ImageField(upload_to = 'pics')
    kcrop_name=models.CharField(max_length = 50)
    kcrop_description=models.TextField()
    kcrop_url=models.CharField(max_length = 50)