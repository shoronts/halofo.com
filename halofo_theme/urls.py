from django.urls import path
from .views import HalofoTheme as theme


urlpatterns = [
    path('', theme.home, name='home'),
    path('about/', theme.about, name='about'),
    path('privacy-policy/', theme.privacy_policy, name='privacy_policy' ),
    path('contact/', theme.contact, name='contact'),
]