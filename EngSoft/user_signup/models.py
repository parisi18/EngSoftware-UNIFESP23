from django.db import models
import uuid

class Usuario(models.Model):
    cpf = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)
    cep = models.CharField(max_length=10)
    email = models.EmailField()
    data_nasc = models.DateField()

class Pet(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    raca = models.CharField(max_length=50)
    idade = models.PositiveIntegerField()
    nome = models.CharField(max_length=100)
    dono = models.ForeignKey(Usuario, on_delete=models.CASCADE)

class FichaDeVacina(models.Model):
    vacina = models.CharField(max_length=100)
    data_vacina = models.DateField()
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)

class Veterinario(models.Model):
    cpf = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)
    crmv = models.CharField(primary_key=True, max_length=10, default=None)
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100, default=None)
    tel = models.CharField(max_length=15)
    cep = models.CharField(max_length=10)
    email = models.EmailField()
    data_nasc = models.DateField()

class ClinicaVeterinaria(models.Model):
    id = models.AutoField(primary_key=True)
    tel = models.CharField(max_length=15)
    endereco = models.CharField(max_length=100, default=None)
    num = models.PositiveIntegerField()
    cep = models.CharField(max_length=10)
    plano = models.CharField(max_length=15, default=None)
    cnpj = models.CharField(max_length=15, default=None)
    vet_resp = models.ForeignKey(Veterinario, on_delete=models.CASCADE)
    email = models.EmailField()