# tests/test_models.py
import pytest
from django.core.files.uploadedfile import SimpleUploadedFile
from imageupload.models import AnimalCard
import cv2
import os
import sys

root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

@pytest.mark.django_db
def test_create_animal_card():
    
    img_file_path = os.path.join(root_path, 'imageupload_samples/dog_sample.jpg')

    # Uma imagem simples carregada como exemplo
    image = cv2.imread(img_file_path)

    # Cria uma instancia simples de AnimalCard
    animal_card = AnimalCard.objects.create(
        animal_name="Test Animal",
        animal_profile_image=image,
        owner_name="Test Owner",
        owner_address="Test Address",
    )

    # Puxa do database o AnimalCard
    retrieved_animal_card = AnimalCard.objects.get(pk=animal_card.animal_id)

    # Verifica o retorno do DB com o teste criado
    assert retrieved_animal_card.animal_name == "Test Animal"
    assert retrieved_animal_card.owner_name == "Test Owner"
    assert retrieved_animal_card.owner_address == "Test Address"

