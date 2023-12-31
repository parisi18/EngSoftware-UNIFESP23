import traceback
from django.shortcuts import render
from .models import ModelImage
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.core.files.storage import FileSystemStorage
from .utils import initPrediction
from EngSoft.settings import BASE_DIR
from imageupload.models import AnimalCard

def image_view(request, animal_id):
    # A imagem carregada pela interface
    image = ModelImage.objects.filter(name='example').first()

    # A predicao default
    resultado_predicao = 'None'

    # Se houver imagem chama a predicao
    if image:
        resultado_predicao = predicao(request)

    # Carrega o objeto da ficha do animal
    animal = AnimalCard.objects.get(animal_id=animal_id)

    context = {'image': image, 'res_pred': resultado_predicao,
               'animal_name': animal.animal_name, 'owner_name': animal.owner_name, 
               'owner_address':animal.owner_address}

    return render(request, 'image_display.html', context)

@require_http_methods(['POST'])
def upload_image(request):
    if 'image' not in request.FILES:
        return JsonResponse({'erro': 'Nenhuma imagem fornecida.'}, status=400)

    image_carregada = request.FILES['image']
    nome_da_image = image_carregada.name

    # Salva a imagem em um local temporario
    fs = FileSystemStorage()
    fs.save(nome_da_image, image_carregada)

    return JsonResponse({'message': 'Imagem enviada com sucesso!'})

@csrf_exempt
@require_http_methods(['POST'])
def predicao(request):
    try:
        if 'image' not in request.FILES:
            return JsonResponse({'erro': 'Nenhuma imagem fornecida.'}, status=400)

        uploaded_image = request.FILES['image']
        uploaded_image_name = uploaded_image.name

        # diretorio de upload quando em desenvolvimento ou producao
        destination_folder = f'{BASE_DIR}/media/prediction/images/{uploaded_image_name}'

        # Salva a imagem carregada em um local temporario
        fs = FileSystemStorage()
        image_path = fs.save(destination_folder, uploaded_image)

        # Correcao na string para que ela contemple a base app/Engsoft/media
        image_path = f'{BASE_DIR}/media/{image_path}'

        # Inicializa a predicao
        label_and_score = initPrediction(image_path)
        return JsonResponse({'result': label_and_score})

    except Exception as e:

        # Log do exception com traceback
        traceback.print_exc()

        return JsonResponse({'erro': 'Ocorreu um erro interno no servidor.' + e})