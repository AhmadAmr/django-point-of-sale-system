# Generated by Django 3.1.7 on 2021-03-29 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('POS', '0007_itemlocation_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemlocation',
            name='location_name',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
