# Generated by Django 3.0 on 2020-09-28 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0002_auto_20200925_0819'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='rubro',
            field=models.CharField(default='Rubro...', max_length=30),
        ),
    ]
