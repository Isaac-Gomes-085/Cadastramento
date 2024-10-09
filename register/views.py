from django.views.generic import ListView, CreateView
from register.models import Clients_SobralPalacio

class Clients_Sobral_Palacio(ListView):
    model = Clients_SobralPalacio
    template_name = "register/home.html"
    context_object_name = "clients"