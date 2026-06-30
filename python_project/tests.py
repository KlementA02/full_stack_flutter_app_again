from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient


class PokemonApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='trainer', password='secret123')
        self.token = Token.objects.create(user=self.user)

    def test_get_all_pokemon_requires_valid_token(self):
        response = self.client.get('/pokedex/api/', HTTP_AUTHORIZATION=f'Token {self.token.key}')

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), dict)
