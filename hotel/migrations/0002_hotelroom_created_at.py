# Generated by Django 5.1.7 on 2025-03-19 21:20

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotelroom',
            name='created_at',
            field=models.DateField(auto_now_add=True, 
                                   default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
