# Generated by Django 5.0.2 on 2024-02-29 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uzytkownicy', '0002_alter_customuser_inne'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='inne',
            field=models.TextField(blank=True, max_length=1024, null=True),
        ),
    ]