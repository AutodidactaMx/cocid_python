# Generated by Django 4.0.4 on 2022-05-14 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apptablero', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ventas',
            name='rama',
            field=models.CharField(max_length=50),
        ),
    ]
