# Generated by Django 3.2.4 on 2021-07-22 04:37

import Home.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0005_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='file',
            field=models.ImageField(blank=True, default='1.jpg', null=True, upload_to=Home.models.upload_image_path),
        ),
    ]