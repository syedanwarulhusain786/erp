# Generated by Django 4.2.4 on 2023-11-14 23:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0011_rename_expiry_date_sales_delivery_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sales',
            old_name='delivery_date',
            new_name='delivery_datesale',
        ),
    ]