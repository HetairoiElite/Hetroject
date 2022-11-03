
from django.test import TestCase
from .models import *
from django.contrib.auth import authenticate, login
from django.test import Client
from django.contrib.sessions.models import Session

# Create your tests here.

# login Test


class LoginTest(TestCase):
    def setUp(self):
        self.user = Usuario.objects.create_user(
            username='Hetairoi', password='Celita1+',
        )

        self.client = Client()

    def test_login(self):

        logged_in = self.client.login(username='Hetairoi', password='Celita1+')

        print("\n")
        print("Session:")
        print("Duración:", self.client.session.get_expiry_age())
        print("Fecha de expiración:",
              self.client.session.get_expiry_date())
        print("Expira cuando cirra navegador:",
              self.client.session.get_expire_at_browser_close())
        print("Duracion cookie:", self.client.session.get_session_cookie_age())
        print("Session Key:", self.client.session.session_key)
        print("Session id:", self.client.session.get('_auth_user_id'))
        
        # Nombre de usuario
        user = Usuario.objects.get(pk=self.client.session.get('_auth_user_id'))
        print("Nombre de usuario:", user.username)
        
        self.assertTrue(logged_in)
