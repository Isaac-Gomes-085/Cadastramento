from django.views.generic import ListView, CreateView
from register.models import Gas_Station_SobralPalacio, DriverList

class Clients_Sobral_Palacio(ListView):
    model = Gas_Station_SobralPalacio
    template_name = "register/home.html"
    context_object_name = "gas_stations"

class DriverList_Gas_Station(ListView):
    model = DriverList
    template_name = "register/drivers.html"
    context_object_name = "drivers"