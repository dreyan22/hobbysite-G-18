# Generated by Django 5.0.3 on 2024-03-20 01:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('merchstore', '0003_product'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['name']},
        ),
    ]
