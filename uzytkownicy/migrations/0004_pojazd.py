# Generated by Django 5.0.2 on 2024-03-01 11:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("uzytkownicy", "0003_alter_customuser_inne"),
    ]

    operations = [
        migrations.CreateModel(
            name="Pojazd",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("numer_rejestracyjny", models.CharField(max_length=12)),
                (
                    "wlasciciel",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
