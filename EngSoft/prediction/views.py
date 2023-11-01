import traceback
from django.shortcuts import render
from .models import ModelImage
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.core.files.storage import FileSystemStorage
from .utils import initPrediction

# Load your TensorFlow model here

def image_view(request):
    # Your existing code for displaying the image
    image = ModelImage.objects.filter(name='example').first()

    resultado_predicao = 'None'

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
    fs.save(uploaded_image_name, uploaded_image)

    # Send a response indicating successful upload
    return JsonResponse({'message': 'Imagem enviada com sucesso!'})

@csrf_exempt
@require_http_methods(['POST'])
def predicao(request):
    try:
        if 'image' not in request.FILES:
            return JsonResponse({'erro': 'Nenhuma imagem fornecida.'}, status=400)

        uploaded_image = request.FILES['image']
        uploaded_image_name = uploaded_image.name
        
        # Save the uploaded image to a temporary location
        fs = FileSystemStorage()
        image_path = fs.save(uploaded_image_name, uploaded_image)

        label_and_score = initPrediction(image_path)
        return JsonResponse({'result': label_and_score})

    except Exception as e:
        # Log the exception
        traceback.print_exc()  # This will print detailed exception information to the console

        # Return an error response
        return JsonResponse({'erro': 'Ocorreu um erro interno no servidor.'})