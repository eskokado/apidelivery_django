from django.db import models

from clients.models import Client


class Address(models.Model):
    number = models.CharField(max_length=50, null=False)
    complement = models.CharField(max_length=100, blank=True, null=True)
    zip_code = models.CharField(max_length=8, null=False)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='addresses')

    class Meta:
        db_table = 'addresses'
