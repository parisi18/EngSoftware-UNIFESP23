from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

class RegisterPageTests(TestCase):
    username = 'newuser'
    email = 'test@email.com'

    # Testa se a página de registro está acessível
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')

    # Testa se o formulário de registro está acessível
    def test_register_form(self):
        new_user = get_user_model().objects.create_user(
            self.username, self.email
        )
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()
                         [0].username, new_user.username)
        self.assertEqual(get_user_model().objects.all()
                         [0].email, new_user.email)
        