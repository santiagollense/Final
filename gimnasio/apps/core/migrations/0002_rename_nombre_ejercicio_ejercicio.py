# Generated by Django 5.0.1 on 2024-02-02 19:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ejercicio',
            old_name='nombre',
            new_name='ejercicio',
        ),
    ]