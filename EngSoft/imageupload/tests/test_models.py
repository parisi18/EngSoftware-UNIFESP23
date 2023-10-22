# tests/test_models.py
import pytest
from imageupload.models import AnimalCard
import cv2
import os

root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

@pytest.mark.django_db
def test_create_animal_card():
    
    # Cria uma instancia simples de AnimalCard
    animal_card = AnimalCard.objects.create(
        animal_name="Test Animal",
        owner_name="Test Owner",
        owner_address="Test Address",
    )

    # Puxa do database o AnimalCard
    retrieved_animal_card = AnimalCard.objects.get(pk=animal_card.animal_id)
    
    # Verifica o retorno do DB com o teste criado
    assert retrieved_animal_card.animal_name == "Test Animal"
    assert retrieved_animal_card.owner_name == "Test Owner"
    assert retrieved_animal_card.owner_address == "Test Address"