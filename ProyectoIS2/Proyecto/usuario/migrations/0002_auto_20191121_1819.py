# Generated by Django 2.2.7 on 2019-11-21 18:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto', '0001_initial'),
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='perfil_redes',
        ),
        migrations.AddField(
            model_name='usuario',
            name='proyecto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='proyecto.Proyecto'),
        ),
    ]
