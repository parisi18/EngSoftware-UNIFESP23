from django import forms
from .models import AnimalCard


class CardForm(forms.ModelForm):
    class Meta:
        model = AnimalCard
        fields = ['animal_profile_image', 'animal_name', 'owner_name',
                  'owner_address']  # here we use the model field names

        labels = {
            'animal_profile_image': 'Imagem de perfil do animal',
            'animal_name': 'Nome do animal',
            'owner_name': 'Nome do dono',
            'owner_address': 'Endereço',
        }
