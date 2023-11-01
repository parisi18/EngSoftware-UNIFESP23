from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import tensorflow as tf
import numpy as np
from PIL import Image
from EngSoft.settings import BASE_DIR

def image_view(request):
    # get an image object from the database
    try:
        image = Image.objects.filter(name='example').first()
        # resultado_predicao = predicao(request)
    except:
        image = None

    # pass the image object as context data
    # context = {'image': image,
    #            'pred_res': resultado_predicao}

    context = {'image': image}
    # render the template with the context data
    return render(request, 'image_display.html', context)


# Carregue seu modelo TensorFlow aqui
modelo = tf.keras.models.load_model(f'{BASE_DIR}/prediction/model/meu_modelo.h5') 

@csrf_exempt
@require_http_methods(['POST'])
def predicao(request):
    if 'imagem' not in request.FILES:
        return JsonResponse({'erro': 'Nenhuma imagem fornecida.'}, status=400)

    imagem = Image.open(request.FILES['imagem'])
    # Pré-processar a imagem conforme necessário para o seu modelo
    imagem = np.array(imagem)
    imagem = imagem / 255.0  # Exemplo de normalização
    imagem = np.expand_dims(imagem, axis=0)

    # Faça a predição
    predicao = modelo.predict(imagem)
    
    # Converta a predição para texto (ajuste conforme necessário)
    resultado_texto = str(predicao)

    return resultado_texto