from django.db import models


# Create your models here.
class place(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='media')
    desc=models.TextField()
    price=models.IntegerField()
    Offer=models.BooleanField(default=False)
class blog(models.Model):
    date=models.CharField(max_length=100)
    img=models.ImageField(upload_to='media')
    month=models.CharField(max_length=100)
    titleb=models.CharField(max_length=100)
    titles=models.CharField(max_length=100)
    desc=models.CharField(max_length=100)

