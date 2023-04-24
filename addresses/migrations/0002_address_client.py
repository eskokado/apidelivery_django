# Generated by Django 4.2 on 2023-04-24 12:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("clients", "0001_initial"),
        ("addresses", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="address",
            name="client",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="addresses",
                to="clients.client",
            ),
            preserve_default=False,
        ),
    ]