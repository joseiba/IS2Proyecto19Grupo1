# Generated by Django 2.2.6 on 2019-12-16 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0002_auto_20191215_2218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='fecha_modificacion',
            field=models.DateField(default=1),
            preserve_default=False,
        ),
    ]
