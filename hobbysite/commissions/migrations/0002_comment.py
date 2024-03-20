# Generated by Django 5.0.3 on 2024-03-20 01:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commissions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('commission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='commissions.commission')),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]
