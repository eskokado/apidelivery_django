from django.db import models


class Supplier(models.Model):
    name = models.CharField(max_length=150, null=False)
    email = models.EmailField(max_length=150, null=False, unique=True)

    class Meta:
        db_table = 'suppliers'
