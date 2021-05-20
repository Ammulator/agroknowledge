from django.db import models

# Create your models here.
class news(models.Model):

    news_image= models.ImageField(upload_to = 'pics')
    news_date= models.CharField(max_length=100)
    news_title= models.CharField(max_length=100)
    news_description= models.TextField()
    news_url= models.CharField(max_length=300)