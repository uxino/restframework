# Generated by Django 5.1 on 2024-08-15 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('haberler', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='makale',
            name='guncelleme_tarihi',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='makale',
            name='yaratilma_tarihi',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
