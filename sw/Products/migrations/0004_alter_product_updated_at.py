# Generated by Django 3.2.4 on 2021-08-11 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0003_alter_product_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='updated_at',
            field=models.DateField(auto_now=True),
        ),
    ]
