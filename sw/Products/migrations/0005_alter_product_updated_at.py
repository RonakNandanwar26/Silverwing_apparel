# Generated by Django 3.2.4 on 2021-08-11 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0004_alter_product_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]