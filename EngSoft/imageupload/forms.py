from django import forms
from .models import AnimalCard

# como django nao possui um campo de multiplos arquivos, precisamos definir um manualmente
class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result


class CardForm(forms.ModelForm):
    # instancio um campo de multiplos arquivos.Usamos o atributo 
    # widget=forms.ClearableFileInput(attrs={'multiple': True}) 
    # para permitir a selecao multipla de arquivos
    animal_images = MultipleFileField(widget=MultipleFileInput(
        attrs={'multiple': True, 'id': 'id_animal_images'}))

    class Meta:
        model = AnimalCard
        fields = ['animal_profile_image', 'animal_name', 'owner_name', 'owner_address',
                  'animal_images']  # here we use the model field names

        labels = {
            'animal_profile_image': 'Imagem de perfil do animal',
            'animal_name': 'Nome do animal',
            'owner_name': 'Nome do dono',
            'owner_address': 'Endereço',
            'animal_images': 'Adicionar imagens',
        }
