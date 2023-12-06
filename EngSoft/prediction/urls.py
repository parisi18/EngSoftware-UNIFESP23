from django.urls import path
from .views import image_view, upload_image, predicao

urlpatterns = [
    path('image/<uuid:animal_id>/', image_view, name='image'),
    path('upload_image/', upload_image, name='upload_image'),  # Add this line
    path('predicao/', predicao, name='predicao'),
]