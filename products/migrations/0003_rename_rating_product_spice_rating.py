# Generated by Django 4.2.1 on 2023-06-28 20:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_category_options_remove_product_image_url_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='rating',
            new_name='spice_rating',
        ),
    ]
