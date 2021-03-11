from django.db import models

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=150)
    uname=models.CharField(max_length=150)
    university=models.CharField(max_length=150,default="daiict")
    desc=models.TextField()
