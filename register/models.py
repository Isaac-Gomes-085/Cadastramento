from django.db import models

class Clients_SobralPalacio(models.Model):
    fantasy_name_client = models.CharField(max_length=40, null=False)
    code_client = models.IntegerField(null=False)