# Generated by Django 4.0.4 on 2022-05-08 03:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apppersonal', '0009_persona_sueldo_alter_persona_fecha_registro'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='altura',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='fecha_registro',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 7, 22, 11, 51, 247884)),
        ),
    ]
