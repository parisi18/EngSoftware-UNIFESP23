from django.shortcuts import render
from .models import ModelImage
from PIL import Image as imgPil
from EngSoft.settings import BASE_DIR
import tensorflow as tf
import numpy as np
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.core.files.storage import FileSystemStorage

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

@require_http_methods(['POST'])
def upload_image(request):
    if 'image' not in request.FILES:
        return JsonResponse({'erro': 'Nenhuma imagem fornecida.'}, status=400)

    uploaded_image = request.FILES['image']
    uploaded_image_name = uploaded_image.name

    # Save the uploaded image to a temporary location
    fs = FileSystemStorage()
    image_path = fs.save(uploaded_image_name, uploaded_image)

    # Send a response indicating successful upload
    return JsonResponse({'message': 'Imagem enviada com sucesso!'})

@csrf_exempt
@require_http_methods(['POST'])
def predicao(request):
    if 'image' not in request.FILES:
        return JsonResponse({'erro': 'Nenhuma imagem fornecida.'}, status=400)

    uploaded_image = request.FILES['image']
    uploaded_image_name = uploaded_image.name

    # Save the uploaded image to a temporary location
    fs = FileSystemStorage()
    image_path = fs.save(uploaded_image_name, uploaded_image)
    imagem = imgPil.open(image_path)

    # Preprocess the image as necessary for your model
    imagem = np.array(imagem)
    imagem = imagem / 255.0  # Example normalization
    imagem = np.expand_dims(imagem, axis=0)

    # Make the prediction
    predicao = modelo.predict(imagem)

    # Convert the prediction to text (adjust as necessary)
    resultado_texto = str(predicao)

    return JsonResponse({'result': resultado_texto})
