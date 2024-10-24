from django.urls import path
from .views import (index, register, profile_view, about, contact, 
                    edit_profile_view, like, cotizar, resultado_cotizacion
                    )


urlpatterns = [
    path('', index, name='home'),
    
    path('accounts/register', register, name='register'),
    
    path('profile', profile_view, name='profile'),
    path('profile/edit/', edit_profile_view, name='edit_profile'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
#___________________________________________________________________________________________________
#███████████████████████████████████████████████████████████████████████████████████████████████████
    path('like/<int:noticia_id>/', like, name='like'),  # Ruta para los likes
    path('cotizar/', cotizar, name='cotizar'),
    path('resultado_cotizacion/', resultado_cotizacion, name='resultado_cotizacion'),
]