# Generated by Django 4.2.1 on 2023-07-02 12:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_rename_spice_rating_product_spice'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='spice',
            new_name='spice_rating',
        ),
    ]
