# Generated by Django 4.2.1 on 2023-07-02 11:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_rename_rating_product_spice_rating'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='spice_rating',
            new_name='spice',
        ),
    ]