# Generated by Django 5.0.1 on 2024-02-06 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_diasemana_alter_rutina_dia_semana'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rutina',
            name='dia_semana',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
