# Generated by Django 4.2.3 on 2023-07-17 08:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("auctions", "0003_listings_category"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Listings",
            new_name="Listing",
        ),
    ]
