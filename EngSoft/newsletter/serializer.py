# Create your models here.
from rest_framework import serializers

# Ira gerar o prompt para cadastro do email
class EmailSubscriptionSerializer(serializers.Serializer):
    email = serializers.EmailField()