# Generated by Django 4.2.3 on 2023-07-17 08:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("auctions", "0005_alter_listing_id"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Listing",
        ),
    ]
