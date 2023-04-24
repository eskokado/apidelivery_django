# Generated by Django 4.2 on 2023-04-24 12:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("suppliers", "0001_initial"),
        ("addresses", "0002_address_client"),
        ("orders", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="address_of_delivery",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="orders",
                to="addresses.address",
            ),
        ),
        migrations.AddField(
            model_name="order",
            name="supplier",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="orders",
                to="suppliers.supplier",
            ),
        ),
    ]