# Generated by Django 3.0.6 on 2021-02-18 12:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0001_initial'),
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Listing',
            new_name='ListingModel',
        ),
    ]