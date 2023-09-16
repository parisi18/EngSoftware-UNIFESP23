from django.shortcuts import render, redirect
from .forms import CardForm
from .models import AnimalCard, AnimalImage
from django.views.generic.edit import FormView
from django.core.paginator import Paginator  # lida com paginacao no template
# operador que lida com consultas complexas em vários campos do modelo
from django.db.models import Q

# Create your views here.
# As views sao responsaveis por processar solicitacoes http e devolver respostas atraves das rotas
# Cada nova funcionalidade da aplicação deve ter uma view associada para controlá-la
# Em resumo, a camada view é o controlador da aplicação (fazendo uma analogia com MVC)

# Funcao responsavel por passar contexto e carregar toda a interface
def animal_card(request):
    # Lidar com paginacao
    all_cards = AnimalCard.objects.all()
    # segmenta a pagina em 4 itens na lista
    paginator = Paginator(all_cards, 4)
    page_number = request.GET.get('page')
    cards = paginator.get_page(page_number)

    # Instancia um forms
    form = CardForm()

    context = {'cards': cards, 'form': form,
               'totalcards': AnimalCard.objects.count()}

    return render(request, 'animalcard.html', context)

# Lida com o formulário de pesquisa, faz consultas no bd
def process_search(request):
    search_term = request.GET.get('search', '')

    if request.method == 'GET' and search_term != '':
        # Prepara os campos de consulta
        filtered_cards = AnimalCard.objects.filter(
            Q(animal_name__icontains=search_term) |
            Q(owner_name__icontains=search_term) |
            Q(owner_address__icontains=search_term)
        )

        form = CardForm()

        context = {'cards': filtered_cards, 'form': form,
                   'totalcards': filtered_cards.count()}

        return render(request, 'animalcard.html', context)
    return redirect('animalcard')

# view que processa um novo registro no formulário
def process_forms(request):
    if request.method == 'POST':
        # request.POST contém dados como texto do formulário | request.FILES contém dados como arquivos
        form = CardForm(request.POST, request.FILES)
        if form.is_valid():
            card = form.save(commit=False)
            card.save()

            # Processar imagens enviadas e associá-las ao cartão
            for image_file in request.FILES.getlist('animal_images'):
                animal_image = AnimalImage(image=image_file)
                animal_image.save()
                card.animal_images.add(animal_image)

            card.save()
        else:
            print(form.errors)
    return redirect('animalcard')


# Recebe uma requisicao HTTP (GET) para processar junto com o id do animal, o processamento é a remoção do card no banco de dados
def delete_card(request, animal_id):
    animal = AnimalCard.objects.get(pk=animal_id)
    animal.delete()
    return redirect('animalcard')

# Recebe uma requisicao HTTP (POST) para processar junto com o id do animal, o processamento é a edição de campos do card no banco de dados
def edit_card(request, animal_id):
    animal_card = AnimalCard.objects.get(pk=animal_id)
    print(animal_id)

    if request.method == 'POST':
        form = CardForm(request.POST, instance=animal_card)
        if form.is_valid():
            form.save()
    return redirect('animalcard')