# Generated by Django 5.0.3 on 2024-03-20 01:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('merchstore', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='producttype',
            options={'ordering': ['name']},
        ),
    ]
