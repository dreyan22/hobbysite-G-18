# Generated by Django 4.2.10 on 2024-03-20 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_recipeingredient_ingredient_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
