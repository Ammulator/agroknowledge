from django.db import models

# Create your models here.
class Contact(models.Model):
  
  name = models.CharField(max_length=122)
  email = models.CharField(max_length=120)
  phone_no=models.CharField(max_length=10)
  desc = models.TextField()
  date = models.DateTimeField(auto_now_add=True)

