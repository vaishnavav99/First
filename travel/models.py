from django.db import models

# Create your models here.
class Destination(models.Model):

	name = models.CharField(max_length=30)
	img = models.ImageField(upload_to= 'pics',null = True)
	desc = models.TextField()
	price = models.IntegerField()