from django.db import models

class Gas_Station_SobralPalacio(models.Model):
    fantasy_name_gas_station = models.CharField(max_length=40, null=False)
    cnpj_gas_station = models.CharField(primary_key=True, max_length=11, null=False)

class DriverList(models.Model):
    name_driver = models.CharField(max_length=30, null=False)
    business_line = models.CharField(max_length=30)
    cpf_driver = models.CharField(primary_key=True, max_length=11, null=False)

    class Operation(models.TextChoices):
        FOB = 'FOB', 'FOB'
        CIF = 'CIF', 'CIF'
    
    rg_driver = models.CharField(max_length=11, null=False)
    rg_issuer = models.DateField()
    driver_license = models.CharField(max_length=11, null=False)
    category = models.CharField(max_length=1, null=False)
    driver_license_issuer = models.DateField()
    place_of_birth = models.DateField(null=False)
    fone_driver = models.CharField(max_length=11)
    email_driver = models.EmailField(max_length=50)
    pis_driver = models.CharField(max_length=14)
    gas_station_CNPJ = models.ForeignKey(Gas_Station_SobralPalacio, on_delete=models.CASCADE, to_field='cnpj_gas_station')


# class Relaçãoentreasduastabelas:
#     nameGestor = models.CharField(max_length=20)