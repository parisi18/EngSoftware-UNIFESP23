from django.http import HttpResponseNotFound, HttpResponseBadRequest, HttpResponseServerError, HttpResponseNotAllowed, HttpResponseForbidden
from django.template.loader import render_to_string

# page not found - recurso nao encontrado
def error_404_page(request, exception):

    # load_to_string renderiza um template como get_template e chama render.
    # usamos essa abordagem aqui, pois HttpResponse precisa 
    # trabalhar com os códigos de status HTTP, mas não pode 
    # renderizar templates ao mesmo tempo
    content = render_to_string('error_404.html', None, request)

    return HttpResponseNotFound(content)

# internal server error - servidor nao conseguiu processar a requisicao
def error_500_page(request):

    content = render_to_string('error_500.html', None, request)

    return HttpResponseServerError(content)

# unauthorized - cliente nao forneceu credenciais validas para acessar o recurso
def error_401_page(request, exception):

    content = render_to_string('error_401.html', None, request)

    return HttpResponseNotAllowed(content)

# forbidden - cliente autenticado nao tem as permissoes necessarias para acessar o recurso
def error_403_page(request, exception):

    content = render_to_string('error_403.html', None, request)

    return HttpResponseForbidden(content)

# bad request - cliente fez uma requisicao mal formatada ou com itens faltantes
def error_400_page(request, exception):

    content = render_to_string('error_400.html', None, request)

    return HttpResponseBadRequest(content)