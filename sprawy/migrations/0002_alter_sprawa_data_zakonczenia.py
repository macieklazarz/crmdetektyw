# Generated by Django 5.0.2 on 2024-03-03 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sprawy', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sprawa',
            name='data_zakonczenia',
            field=models.DateTimeField(null=True),
        ),
    ]