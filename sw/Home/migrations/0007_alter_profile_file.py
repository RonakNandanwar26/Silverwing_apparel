# Generated by Django 3.2.4 on 2021-07-22 04:41

import Home.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0006_alter_profile_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='file',
            field=models.ImageField(blank=True, default='ronak.jpg', null=True, upload_to=Home.models.upload_image_path),
        ),
    ]
