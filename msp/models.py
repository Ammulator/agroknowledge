from django.db import models

# Create your models here.
class cropmsp(models.Model):

    msp_crop_title= models.CharField(max_length = 50)
    crop_price= models.IntegerField(default=0)
