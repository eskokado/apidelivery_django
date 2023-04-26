from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=150, null=False, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    class Meta:
        db_table = 'products'
