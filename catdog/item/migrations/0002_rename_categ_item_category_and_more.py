# Generated by Django 4.2.4 on 2023-08-27 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='categ',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='desc',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='img',
            new_name='image',
        ),
    ]
