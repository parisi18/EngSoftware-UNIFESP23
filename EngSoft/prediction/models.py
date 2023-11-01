from django.db import models

class ModelImage(models.Model):
    name = models.CharField(max_length=100) # a name for the image
    image = models.ImageField(upload_to='images/') # the image file and its URL
