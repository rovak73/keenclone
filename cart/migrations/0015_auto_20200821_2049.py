# Generated by Django 3.0.8 on 2020-08-21 20:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0014_order_billing_address'),
    ]

    operations = [
        migrations.RenameField(
            model_name='billingaddress',
            old_name='countries',
            new_name='country',
        ),
    ]