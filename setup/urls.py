from django.contrib import admin
from django.urls import path
from register.views import Clients_Sobral_Palacio, DriverList_Gas_Station


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', Clients_Sobral_Palacio.as_view(), name='home'),
    path('drivers/', DriverList_Gas_Station.as_view(), name='drivers')
]
