from django.contrib import admin
from django.urls import path
from register.views import Clients_Sobral_Palacio


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', Clients_Sobral_Palacio.as_view(), name='home')
]
