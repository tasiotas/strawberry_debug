# Generated by Django 4.2.4 on 2023-08-16 13:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_remove_fruit_color_color_color'),
    ]

    operations = [
        migrations.RenameField(
            model_name='color',
            old_name='color',
            new_name='fruit',
        ),
    ]
