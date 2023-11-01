from django.shortcuts import render
from .models import ModelImage
from PIL import Image as imgPil
from EngSoft.settings import BASE_DIR
import tensorflow as tf
import numpy as np
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.core.files.storage import FileSystemStorage  # Add this import

# Load your TensorFlow model here
modelo = tf.keras.models.load_model(f'{BASE_DIR}/prediction/model/meu_modelo.h5') 

def image_view(request):

    # Your existing code for displaying the image
    image = ModelImage.objects.filter(name='example').first()
    resultado_predicao = ''
    if image:
        resultado_predicao = predicao(request)

    context = {'image': image, 'res_pred': resultado_predicao}
    return render(request, 'image_display.html', context)


@csrf_exempt
@require_http_methods(['POST'])
def predicao(request):
    if 'imagem' not in request.FILES:
        return JsonResponse({'erro': 'Nenhuma imagem fornecida.'}, status=400)

    uploaded_image = request.FILES['imagem']
    uploaded_image_name = uploaded_image.name

    # Save the uploaded image to a temporary location
    fs = FileSystemStorage()
    image_path = fs.save(uploaded_image_name, uploaded_image)
    imagem = imgPil.open(image_path)
    # Pré-processar a imagem conforme necessário para o seu modelo
    imagem = np.array(imagem)
    imagem = imagem / 255.0  # Exemplo de normalização
    imagem = np.expand_dims(imagem, axis=0)

    # Faça a predição
    predicao = modelo.predict(imagem)
    
    # Converta a predição para texto (ajuste conforme necessário)
    resultado_texto = str(predicao)

    return resultado_texto