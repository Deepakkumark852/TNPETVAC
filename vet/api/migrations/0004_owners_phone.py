# Generated by Django 3.2 on 2023-07-25 15:14

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20230725_1512'),
    ]

    operations = [
        migrations.AddField(
            model_name='owners',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(default='+91', max_length=128, region=None),
        ),
    ]
