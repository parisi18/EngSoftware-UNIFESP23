from django.test import TestCase
from django.test import Client
from .error_http_500 import ErrorHttp500
from .error_http_401 import ErrorHttp401
from .error_http_403 import ErrorHttp403
from .error_http_400 import ErrorHttp400

# https://docs.djangoproject.com/en/4.2/topics/testing/overview/

# exceptions do Django:
# https://docs.djangoproject.com/en/2.0/ref/exceptions/#suspiciousoperation

# unittest: https://docs.python.org/3/library/unittest.html

# a ideia aqui foi a de verificar se as rotas existem e se retornam os templates

class HttpError(TestCase):
    def test_http_status_code_404(client):
        # instancio um objeto cliente django
        client = Client()

        # faço requisicao GET
        response = client.get('/httperrors/views/error_404_page')

        # verifico se o template correto foi utilizado
        assert 'error_404.html' in [template.name for template in response.templates]

    def test_http_status_code_500(self):
        try:
            with self.assertRaises(ErrorHttp500):
                # emulo a resposta de status 500 do servidor
                raise ErrorHttp500('Make response code 500!')
        except ErrorHttp400:
            with self.assertTemplateUsed('error_500.html'):
                self.client.get('httperrors.views.error_500_page')

    def test_http_status_code_401(self):
        try:
            with self.assertRaises(ErrorHttp401):
                raise ErrorHttp401('Make response code 401!')
        except ErrorHttp401:
            with self.assertTemplateUsed('error_401.html'):
                self.client.get('httperrors.views.error_401_page')

    def test_http_status_code_403(self):
        try:
            with self.assertRaises(ErrorHttp403):
                raise ErrorHttp403('Make response code 403!')
        except ErrorHttp403:
            with self.assertTemplateUsed('error_403.html'):
                self.client.get('httperrors.views.error_403_page')

    def test_http_status_code_400(self):
        try:
            with self.assertRaises(ErrorHttp400):
                raise ErrorHttp400('Make response code 400!')
        except ErrorHttp400:
            with self.assertTemplateUsed('error_400.html'):
                self.client.get('httperrors.views.error_400_page')