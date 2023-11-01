from django.db import models

class ModelImage(models.Model):
    name = models.CharField(max_length=100) # Nome da imagem
    image = models.ImageField(upload_to='images/') # A imagem e o url
