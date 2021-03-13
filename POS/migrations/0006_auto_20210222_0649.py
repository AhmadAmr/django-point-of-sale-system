# Generated by Django 3.1.7 on 2021-02-22 14:49

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('POS', '0005_auto_20210221_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='phone_no',
            field=models.CharField(max_length=11, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:\\d+)*\\Z'), code='invalid', message=None), django.core.validators.MinLengthValidator(11)], verbose_name='Phone number'),
        ),
    ]