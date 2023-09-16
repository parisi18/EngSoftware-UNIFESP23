from django.db import models
import uuid

# Esse modelo serve para representar imagens de animais
class AnimalImage(models.Model):
    image = models.ImageField('Animal images', upload_to='imageupload/animalimages')

# Modelo principal dos dados das fichas dos animais
class AnimalCard(models.Model):
    animal_name = models.CharField('Animal name', max_length=50)
    animal_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    animal_profile_image = models.ImageField('Animal profile image', upload_to='imageupload/animalprofilepic')
    # ManyToManyField referencia o modelo AnimalImage, cada imagem é representada como uma instância de AnimalImage. 
    # related_to é o nome do relacionamento entre esses dois modelos
    animal_images = models.ManyToManyField(AnimalImage, related_name='animal_cards')
    diagnosed_images = models.IntegerField('Diangosed images', null=True)
    verified_images = models.IntegerField('Verified images', null=True)
    owner_name = models.CharField('Owner name', max_length=50)
    owner_address = models.CharField('Owner address', max_length=100)

    # printa o conteudo do modelo sem a necessidade de chamar um metodo especifico
    def __str__(self):
        return f'{self.animal_name}, {self.animal_id}, {self.animal_profile_image}, {self.animal_images}, {self.diagnosed_images}, {self.verified_images}, {self.owner_name}, {self.owner_address}'