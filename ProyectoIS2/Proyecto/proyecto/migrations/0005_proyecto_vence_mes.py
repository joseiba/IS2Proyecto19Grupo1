# Generated by Django 2.2.6 on 2019-12-16 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto', '0004_proyecto_cant_dias_atrasados'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyecto',
            name='vence_mes',
            field=models.CharField(default='NO', max_length=3),
        ),
    ]
