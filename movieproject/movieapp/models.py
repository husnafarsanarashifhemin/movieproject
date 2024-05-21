from django.db import models

# Create your models here.
class Movie(models.Model):
    name=models.CharField(max_length=250)
    desc=models.TextField(max_length=700)
    year=models.IntegerField()

